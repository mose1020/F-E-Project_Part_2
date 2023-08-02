# Step 1: Follow the instructions in README_Setup.md
       If you started already started the setup, you can skip this step.
# Step 2: Open Catkin_ws workspace in vs_code
* open script name: "kovis_ibvs.py"

This script is the main script for the IBVS control.

    if __name__ == '__main__':
    try:
        main(keypoint_selection=True,make_goal_image=False,move_to_startpose=True)
    except rospy.ROSInterruptException:
        pass

### In the Main you have 3 options:
* **keypoint_selection**: If you don't want to use all your feature points. You can select the feature points you want to use. And change kexpoint_selection to True.

* **make_goal_image**: If you want to make a new goal image. You can change make_goal_image to True. This will make a goal image and save it in the folder "goal_image". It's always useful to make a new goal image because of the changing light conditions. After that you can change make_goal_image to False and start the IBVS controller.

* **move_to_startpose**: If you want to move the robot to the startpose. You can change move_to_startpose to True. This will move the robot to the startpose.

# Step 3: Parameters for the IBVS controller

    visual_servoing_controller = VisualServoingController(z=0.24)

Parameter z: is the distance between the camera and the object. Its important to set this parameter correctly. Otherwise the controller will not work correctly

The IBVS controller is programmed in the class VisualServoingController.

# Step 4: Validation
During the Regulation we save parameters in a csv file. You can find the csv file: "scripts/kovis_moduls/keypoints_servoing.csv" The csv file contains the following parameters:

* **iteration_number**: The number of the iteration.
* **delta_loop**: The time between two iterations
* **delta_interference**: The time between two iterations #TODO: What is the difference between delta_loop and delta_interference?
* **delta_extract_featurepoints**: The time to extract the feature points.
* **delta_camera**: The time to get the image from the camera.
* **dp**: Twist / Velocities from the IBVS controller.

keypoints,iteration_number,delta_loop,delta_interference,

Now run the validation script: **kovis_validation.py**

# Start the Programm

The Twist from The IBVS controller is clipped for saftey reasons.
        
    rosrun iaps_ur5e_sim kovis_ibvs.py  






