# Step 1: Start of the robot

* On power-off (red button) 
* Start Robi --> click through 
* Bottom left, green and normalOn power-off (red button) 

# Step 2: open first terminal--> start robot driver

* with cd_catkin 

    ```
    cd catkin_ws;source /opt/ros/noetic/setup.bash;source devel/setup.bash;roslaunch    ur_robot_driver ur5e_bringup.launch robot_ip:=192.168.1.101 kinematics_config:=${HOME}/ur5e_calibration.yaml  


* without cd_cakin: 

    ```
    source /opt/ros/noetic/setup.bash;source devel/setup.bash;roslaunch ur_robot_driver     ur5e_bringup.launch robot_ip:=192.168.1.101 kinematics_config:=${HOME}/ur5e_calibration.yaml  

# Step 3: Switch on the external control in the handheld terminal  

Run --> load Program --> external control --> open --> bottom right play --> Robot from beginning  

In the first terminal appears the message: "Ready to receive control commands".

# Step 4: open second terminal (ctrl+shift+t)--> main launch

* with cd_catkin: 

    ``` 
    cd catkin_ws;source /opt/ros/noetic/setup.bash;source devel/setup.bash;roslaunch iaps_ur5e_sim main.launch 


* without cd cakin: 

    ``` 
    source /opt/ros/noetic/setup.bash;source devel/setup.bash;roslaunch iaps_ur5e_sim main.launch 

# Step 5: open third terminal (ctrl+shift+t)  

Split terminal into three parts --> Source each part

* with cd catkin: 

        cd catkin_ws;source /opt/ros/noetic/setup.bash;source devel/setup.bash 

* without cd catkin: 

        source /opt/ros/noetic/setup.bash;source devel/setup.bash 

# Step 6: Start Twist Controller:

    rosservice call /controller_manager/switch_controller "start_controllers: ['twist_controller']    

    stop_controllers: ['forward_cartesian_traj_controller']  

    strictness: 1  

    start_asap: false

    timeout: 0.0"

Command to start the twist controller. The twist controller is the controller for the IBVS. Stop all the controller that are colliding with the twist controller.

# Step 7: RVIZ 


    rviz 

# Step 8: Termination condition for Saftey

This command is for saftey if you stop the programm the last twist is still active. You have to publish a zero twist. To reset the twist to zero.

    rostopic pub /twist_controller/command geometry_msgs/Twist  

press tab and set everything to zero. 

# Step 9: Go to Readme_KOVIS.md

In this Readme you can find the instructions for the the KOVIS Script and how to run it.
