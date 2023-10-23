<h1 style="text-align:center;">Tutorial 1: Introduction to UAS</h1>
<h2 style="text-align:center;"></h2>

<h4 style>
    <div style="text-align:center;">

Quadcopters and Simulated Flights with Ardupilot

Travis Fields, Justin Nguyen, & Daniel McIntosh 
    </div>
</h4>

## Deliverables 

## Purpose

## Outline 
| Section | Topic | Outcome |
|----------|----------|----------|
| 1.1 | Ardupilot Software In the Loop (SITL) and Gazebo Installation | Gain expertise in installing and initializing simulations using the Ardupilot Flight Controller and Gazebo environment. |
| 1.2 | Mission Planner Installation | Acquire skills in setting up and operating a ground control station, understanding its crucial role in flight test operations |
| 1.3 | Ardupilot Flight Controller | Develop a deep understanding of the flight controller's purpose and grasp how adjusting specific parameters influences the quadcopter's flight performance |
| 1.4 | Manual Flight Tests Using SITL | Attain confidence in executing manual flights within the simulation, and adeptly conduct thorough flight tests to gather essential data |
| 1.5 | Autonomous" Waypoint Navigation with SITL | Master the ability to pre-program waypoints into the flight controller, enabling autonomous navigation, and efficiently collect flight data |


## Overview 
In this tutorial, we will explore Ardupilot Software In the Loop (SITL) and Gazebo installation, gaining expertise in setting up simulations using the Ardupilot Flight Controller and Gazebo environment. We'll learn essential skills in configuring ground control stations, understand the flight controller's parameters, and conduct both manual and autonomous flight tests. By the end, we'll be adept at optimizing quadcopter performance through precise adjustments.

### 1.1 Ardupilot Software In the Loop (SITL) and Gazebo Installation

#### If you have Windows 
- If you have Windows OS, please install **Windows Subsystem for Linux 2** through the following link attached https://learn.microsoft.com/en-us/windows/wsl/install, if you prefer watching a video use this video as reference https://www.youtube.com/watch?v=28Ei63qtquQ&t=9s&ab_channel=TECHDHEE

#### Installing Ardupilot 
If you are on Linux open up a terminal, for those of you who are using Windows Subsystem for Linux open up the WSL2 terminal through Windows Powershell after that enter the following commands 

```bash 
git clone --recursive https://github.com/ArduPilot/ardupilot.git #this downloads the ardupilot repo
cd ardupilot
./waf configure --board sitl           # software-in-the-loop simulator
```
Once you are done compiling ardupilot let's start the simulator 

Enter the following commands and you should see some windows pop up for the flight simulation
```
cd ~/ardupilot/ArduCopter
../Tools/autotest/sim_vehicle.py --map --console
```
![Ardupilot](images/ardu_sitl.png)

#### Installing Gazebo 
It's a little hard to see the simulation so let's install Gazebo to allow us to visually see the quadcopter platform in a 3D environment. 

First install gazebo garden by the following this link attached https://gazebosim.org/docs/garden/install_ubuntu_src

Afterwards follow the link attached https://ardupilot.org/dev/docs/sitl-with-gazebo.html from the **Install the ArduPilot Gazebo Plugin** 

#### Run Gazebo with Ardupilot
Once you are done on a new terminal enter the following command and you should see a quadcopter show up: 
```
gz sim -v4 -r iris_runway.sdf
```

#### Task 1.1
Take a screenshot of your simulation 

### 1.2 Mission Planner Installation 






