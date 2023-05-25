import numpy as np
from os import listdir, path
from PIL import Image, ImageOps
import torch
import torch.utils.data as _data
import torchvision.transforms.functional as F
from PIL import ImageEnhance
import os
# import matplotlib.pyplot as plt
# from skimage import data, io, img_as_ubyte
# from skimage.filters import threshold_multiotsu
# from skimage.color import rgb2gray
# import skimage.util
# from scipy import ndimage
# from scipy.interpolate import splprep, splev


class DataServoStereo(_data.Dataset):
    def __init__(self, arg, train=True,grey=False):
        # arguments are imported from yaml
        self.train = train
        self.im_size = arg.im_size[0]
        self.mean = arg.mean
        self.std = arg.std
        self.brightness = arg.brightness
        self.brightness_true = arg.brightness_true
        #self.saturation = arg.saturation
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

        if self.train:
        # loads only one image at a time
            img,plug_mask_tensor,plug_mask = self.img_processing(path.join(self.data_path,self.ims[index]), self.brightness, self.brightness_true)
        else:
            img = self.img_processing(path.join(self.data_path,self.ims[index]), self.brightness, self.brightness_true)

        if self.train:
            return img,plug_mask_tensor,plug_mask
        else:
            return img
        
        

    def img_processing(self,data_path, brightness, brightness_true):
        
        img = Image.open(data_path)

        if self.train:

            if brightness_true == True:
                min_brightness = brightness[0]
                max_brightness = brightness[1]

            # Wähle einen zufälligen Helligkeitswert innerhalb der Range
                brightness = np.random.uniform(min_brightness, max_brightness)

                enhancer = ImageEnhance.Brightness(img)
                img = enhancer.enhance(brightness)
            


            #safe picture after brigheess adjustment to check the output
                # # Ordner für die gespeicherten Bilder erstellen, wenn er noch nicht existiert
                # save_folder = "dataset/brightness_pictures"
                # os.makedirs(save_folder, exist_ok=True)

                # # Zähler für den Dateinamen
                # counter = len(os.listdir(save_folder)) + 1

                # # Bild speichern
                # save_path = os.path.join(save_folder, f"processed_image_{counter}.jpg")
                # img.save(save_path)
                # print("Image saved to", save_path)
            

        img = self.img_patch(img)

  
        # If the parameter "grey" is true, convert the image to grayscale
        if self.grey:
            img = img.convert('L')
        # Convert the image to a numpy array of type "uint8
        img = np.array(img, np.uint8)

        # Convert the image into a tensor, normalize it with mean and standard deviation
        img = F.to_tensor(img)
        img = F.normalize(img, [self.mean], [self.std])

        if self.train:

            mask_path = data_path.replace('train', 'segmentation_images')
            mask_tensor, mask = self.img_segmention2(mask_path)

        if self.train:
            return img,mask_tensor,mask
        else:
            return img


    def img_segmention2(self,mask_path):

        mask = Image.open(mask_path).convert('1')
        mask = self.img_patch(mask,segmentation=True)
        mask = np.array(mask)
        mask_tensor = torch.from_numpy(mask)

        return mask_tensor, mask
    
    
    def img_patch(self,img,segmentation=False):
        # Calculate the aspect ratio of the image
        img_ratio = img.width / img.height

        # If the image is wider than it is high
        if img_ratio > 1:
            # Scale the width to the desired size and calculate the height while maintaining the aspect ratio
            new_width = self.im_size[0]
            new_height = int(new_width / img_ratio)
        # If the image is taller than it is wide
        else:
            # Scale the height to the desired size and calculate the width while maintaining the aspect ratio
            new_height = self.im_size[1]
            new_width = int(new_height * img_ratio)

        # Resize the image to the calculated size while maintaining the aspect ratio
        img = img.resize((new_width, new_height), resample=Image.BICUBIC)

        # Add black borders to the left and right or top and bottom of the image to make it the desired size
        delta_w = self.im_size[0] - new_width
        delta_h = self.im_size[1] - new_height
        pad_width = delta_w // 2
        pad_height = delta_h // 2
        padding = (pad_width, pad_height, delta_w - pad_width, delta_h - pad_height)
        if segmentation:
            img = ImageOps.expand(img, border=padding, fill=(0))
        else:
            img = ImageOps.expand(img, border=padding, fill=(255,255,255))

        # Return the scaled and centered image
        return img