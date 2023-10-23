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

## 1.1 Ardupilot Software In the Loop (SITL) and Gazebo Installation

### If you have Windows 
- If you have Windows OS, please install **Windows Subsystem for Linux 2** through the following link attached https://learn.microsoft.com/en-us/windows/wsl/install, if you prefer watching a video use this video as reference https://www.youtube.com/watch?v=28Ei63qtquQ&t=9s&ab_channel=TECHDHEE

### Installing Ardupilot 
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

### Installing Gazebo 
It's a little hard to see the simulation so let's install Gazebo to allow us to visually see the quadcopter platform in a 3D environment. 

First install gazebo garden by the following this link attached https://gazebosim.org/docs/garden/install_ubuntu_src

Afterwards follow the link attached https://ardupilot.org/dev/docs/sitl-with-gazebo.html from the **Install the ArduPilot Gazebo Plugin** 

#### Run Gazebo with Ardupilot
Once you are done on a new terminal enter the following command and you should see a quadcopter show up: 
```
gz sim -v4 -r iris_runway.sdf
```

### Task 1.1
Take a screenshot of your simulation 

## 1.2 Mission Planner Installation 
Mission Planner is a powerful and versatile ground control station software designed for planning, executing, and analyzing unmanned vehicle missions. Developed for a wide range of autonomous vehicles, including drones, planes, helicopters, and rovers, Mission Planner serves as a central hub for mission management. Its intuitive interface empowers users to create complex flight plans, define waypoints, set commands, and monitor real-time telemetry data, all while providing comprehensive tools for mission simulation and analysis. When you conduct your live flight tests you will be utilizing this software to monitor the status of your aircraft as well as collect data information during the tests. In this tutorial you will be utilizing Mission Planner to collect flight information of your simulated quadcopter, but first off let's install Mission Planner

### If you have Windows
If you have windows please follow this link attached https://ardupilot.org/planner/docs/mission-planner-installation.html and follow the **Windows** instructions

### If you have Ubuntu/Linux
Open up a terminal and do the following 
Install mono 
```bash
sudo apt install ca-certificates gnupg
sudo gpg --homedir /tmp --no-default-keyring --keyring /usr/share/keyrings/mono-official-archive-keyring.gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
echo "deb [signed-by=/usr/share/keyrings/mono-official-archive-keyring.gpg] https://download.mono-project.com/repo/ubuntu stable-focal main" | sudo tee /etc/apt/sources.list.d/mono-official-stable.list
sudo apt update
```
If you have windows please follow this link attached https://ardupilot.org/planner/docs/mission-planner-installation.html and follow the **Linux** instructions. **If you did the following terminal commands, you have already did done the install the latest version of MONO skip to the next step**


### Run Ardupilot Gazebo and Mission Planner 
With Ardupilot, Gazebo, and Mission Planner all installed let's run all three and have them connect to each other.

## 1.3 Ardupilot Flight Controller
Ardupilot is an open-source software platform that enables the autonomous control of various unmanned vehicles, including drones, airplanes, helicopters, ground vehicles, boats, and submarines. Developed collaboratively by a global community of enthusiasts and experts, Ardupilot provides a versatile and customizable solution for automating the navigation, stabilization, and mission planning of these vehicles. Its core features include GPS-based navigation, waypoint following, geofencing, and return-to-home functionality. Ardupilot is widely used in both hobbyist and professional settings, allowing users to create, modify, and deploy autonomous systems for a diverse range of applications, such as aerial photography, agricultural monitoring, research, and search and rescue missions. Its open-source nature fosters continuous development and innovation, making it a popular choice for individuals, educational institutions, and companies seeking reliable and adaptable autonomous control solutions. 

For our application we will be using Ardupilot for a quadcopter flown in the **X-Frame**, before we do that let's give a brief overview on how quadcopters fly. 

### How does a Quadcopter fly? 
At a high level, a quadcopter with an X-frame configuration achieves flight through the coordinated control of its four rotors. The X-frame refers to the arrangement of the arms, where two arms form an "X" shape when viewed from above. Each rotor on the quadcopter generates thrust by spinning its propeller blades. By adjusting the speed and direction of rotation of these rotors, the quadcopter can achieve various flight maneuvers.

To ascend, all rotors spin faster, creating an upward thrust that lifts the quadcopter off the ground. To descend, the rotor speeds are reduced. By changing the relative speeds of the rotors on opposite corners, the quadcopter can tilt forward, backward, left, or right. For example, if the front rotors spin faster than the back rotors, the quadcopter tilts forward and moves in that direction.

Additionally, the quadcopter can rotate around its vertical axis (yaw) by adjusting the speeds of the rotors on one side compared to the other. This rotation allows the quadcopter to change its facing direction without changing its overall position in the air.

![Ardupilot](images/quad_x.png)
The flight controller (Ardupilot), a central component of the quadcopter, manages and balances the speeds of these rotors based on input from sensors such as accelerometers and gyroscopes. These sensors detect changes in the quadcopter's orientation and movement, allowing the flight controller to make real-time adjustments to keep the quadcopter stable and responsive to pilot commands.

You will notice that each of these motors are in opposite orientations. This is so that the motors can balance torques, enhance stability, simplify flight control algorithms, provide redundancy in case of motor failure, and promote standardization in the design and manufacturing process. This setup ensures a stable and predictable flight experience. 

### Control Gains
The way the flight controller "controls" a quadcopter to move to a respective position, attitude, attitude rate is through a control algorithm known as a **Proportional Integral Derivative** (PID Controller), we'll d

Please watch this video https://www.youtube.com/watch?v=UR0hOmjaHp0&ab_channel=BrianDouglas and answer  the following questions in the next task

## Task 1.3.1a 
- Briefly explain the role of each term (Proportional, Integral, Derivative) in the control loop.
- Consider a quadcopter controlled by a PID controller. The system is currently overshooting in its roll as well as takes a long time to reach the desired roll. Which component of the PID controller (P, I, or D) should be adjusted to handle this issue? 

### Adjusting the Control Gains with Ardupilot 
For this section we will alter the PID gains for the roll and pitch controllers, these parameters in Ardupilot are known as: 

```
    ATC_RAT_PIT_P 

    ATC_RAT_PIT_I

    ATC_RAT_PIT_D

    ATC_RAT_RLL_P

    ATC_RAT_RLL_I

    ATC_RAT_RLL_D
```
Refer []


## Task 1.3.1b
Run your [Gazebo Simulation](#run-ardupilot-gazebo-and-mission-planner)



<!-- ## Subtitle 1 (Heading 2)

## Subtitle 1 (Heading 2) {#subtitle1}

[Link Text](#subtitle1) -->