import numpy as np
from os import listdir, path
from PIL import Image, ImageOps
import torch
import torch.utils.data as _data
import torchvision.transforms.functional as F
import matplotlib.pyplot as plt
from skimage import data, io, img_as_ubyte
from skimage.filters import threshold_multiotsu
from skimage.color import rgb2gray
import skimage.util
from scipy import ndimage
from scipy.interpolate import splprep, splev


class DataServoStereo(_data.Dataset):
    def __init__(self, arg, train=True,grey=False):
        # arguments are imported from yaml
        self.train = train
        self.im_size = arg.im_size[0]
        self.mean = arg.mean
        self.std = arg.std
        self.data_path = path.join(arg.dir_dataset, 'train' if train else 'test')
        self.ims = sorted(listdir(self.data_path))
        self.grey = grey
        self.obj_class = arg.obj_class
        self.threshold = arg.threshold

        print('{} {} data loaded'.format(len(self.ims), 'training' if train else 'testing'))


    def __getitem__(self, index):
        try:
            return self.data_transform(index)
        except Exception as e:
    
            print(f"Error occurred while getting item picture {self.ims[index]}: {e}")
            return None
    
    def __len__(self):
        return len(self.ims)

    def data_transform(self, index):

        # loads only one image at a time
        img,plug_mask_tensor,plug_mask = img_processing(path.join(self.data_path,self.ims[index]),
                             self.im_size,mean=self.mean,std=self.std,grey=self.grey)
        
        #print(self.ims[index])
        return img,plug_mask_tensor,plug_mask
        

def img_processing(data_path, im_size, mean, std, grey):
    
    img = Image.open(data_path)
    img = img_patch(img, im_size)
    
    #outS_tensor,outS = img_segmention(img)
    plug_mask_tensor, plug_mask,_ = img_segmention(img)


    # If the parameter "grey" is true, convert the image to grayscale
    if grey:
        img = img.convert('L')

    # Convert the image to a numpy array of type "uint8
    img = np.array(img, np.uint8)

    # Convert the image into a tensor, normalize it with mean and standard deviation
    img = F.to_tensor(img)
    img = F.normalize(img, [mean], [std])

    return img,plug_mask_tensor,plug_mask




def img_segmention(img):

    img_resized = np.array(img)
    img_ski = skimage.util.img_as_float32(img_resized)
    img_gray= rgb2gray(img_ski)


    # Apply multi-Otsu threshold 
    thresholds = threshold_multiotsu(img_gray, classes=3)

    # Digitize (segment) original image into multiple classes.
    # np.digitize assign values 0, 1, 2, 3, ... to pixels in each class.
    regions = np.digitize(img_gray, bins=thresholds)
    mask_1 = img_as_ubyte(regions)  #Convert 64 bit integer values to uint8



    board_mask = mask_1.copy()
    board_mask[board_mask == 0] = 9
    board_mask[board_mask == 3] = 0
    board_mask[board_mask == 2] = 0
    board_mask[board_mask == 1] = 0

    # Find the bounding box of the first class
    y, x = np.where(board_mask == 9)


    # Pass a B-spline through the points
    tck, u = splprep([x, y], s=0, per=False)

    # Create a new array containing the B-spline
    new_x, new_y = splev(np.linspace(0, 1, 36000), tck)
    board_mask = np.zeros_like(board_mask)
    board_mask[np.round(new_y).astype(int), np.round(new_x).astype(int)] = 1
   
    img_gray_board = img_gray.copy()
    img_gray_board[board_mask == 0] = 0


    # Apply multi-Otsu threshold 
    thresholds = threshold_multiotsu(img_gray_board, classes=4)

    # Digitize (segment) original image into multiple classes.
    #np.digitize assign values 0, 1, 2, 3, ... to pixels in each class.
    regions = np.digitize(img_gray_board, bins=thresholds)
    mask_2 = img_as_ubyte(regions)  #Convert 64 bit integer values to uint8


    plug_mask = mask_2.copy()
    # final_mask[final_mask == 0] = 9
    plug_mask[plug_mask == 3] = 0
    # final_mask[final_mask == 2] = 0
    plug_mask[plug_mask == 1] = 0



    # identify the coordinates of all 2s values in the array
    coords = np.where(plug_mask == 2)

    # identify the contiguous ranges of 2s values in the array
    labels, num_labels = ndimage.label(plug_mask == 2)

    # count the number of pixels in each identified area
    counts = np.bincount(labels.flatten())

    # identify the number of the largest area
    largest_label = np.argmax(counts[1:]) + 1

    # determine the boundary of the rectangle around the largest area
    largest_label_mask = (labels == largest_label)
    ys, xs = np.where(largest_label_mask)
    y_min, y_max, x_min, x_max = ys.min(), ys.max(), xs.min(), xs.max()

    # create a new array with the same dimensions as the original array, but with all 2s values set to 0
    plug_mask = np.zeros_like(plug_mask)

    # set all pixels within the boundary of the rectangle to 2 in the new array
    plug_mask[y_min:y_max+1, x_min:x_max+1][largest_label_mask[y_min:y_max+1, x_min:x_max+1]] = 2


    idxs = np.where(plug_mask == 2)

    # Determine the boundaries of the bounding box
    top = np.min(idxs[0])
    left = np.min(idxs[1])
    bottom = np.max(idxs[0])
    right = np.max(idxs[1])

    # Extend the bounding box by 1 pixel in all directions
    top = max(0, top - 1)
    left = max(0, left - 1)
    bottom = min(plug_mask.shape[0] - 1, bottom + 1)
    right = min(plug_mask.shape[1] - 1, right + 1)

    plug_mask[top:bottom+1, left:right+1][plug_mask[top:bottom+1, left:right+1] == 0] = 2

    plug_mask[plug_mask == 2] = 1



    #outS = plug_mask


    plug_mask_tensor = torch.from_numpy(plug_mask.astype(np.int))

    #print("type outS",outS.type())
    

    return plug_mask_tensor, plug_mask, board_mask






def img_patch(img, imsize):
    # Calculate the aspect ratio of the image
    img_ratio = img.width / img.height

    # If the image is wider than it is high
    if img_ratio > 1:
        # Scale the width to the desired size and calculate the height while maintaining the aspect ratio
        new_width = imsize[0]
        new_height = int(new_width / img_ratio)
    # If the image is taller than it is wide
    else:
        # Scale the height to the desired size and calculate the width while maintaining the aspect ratio
        new_height = imsize[1]
        new_width = int(new_height * img_ratio)

    # Resize the image to the calculated size while maintaining the aspect ratio
    img = img.resize((new_width, new_height), resample=Image.BICUBIC)

    # Add black borders to the left and right or top and bottom of the image to make it the desired size
    delta_w = imsize[0] - new_width
    delta_h = imsize[1] - new_height
    pad_width = delta_w // 2
    pad_height = delta_h // 2
    padding = (pad_width, pad_height, delta_w - pad_width, delta_h - pad_height)
    img = ImageOps.expand(img, border=padding, fill=(255,255,255))

    # Return the scaled and centered image
    return img





