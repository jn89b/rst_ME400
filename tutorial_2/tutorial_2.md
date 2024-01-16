<h1 style="text-align:center;">Tutorial 2: Data Analytics</h1>
<h2 style="text-align:center;"></h2>

<h4 style>
    <div style="text-align:center;">

MEC-ENGR 400-0001 and PHYSICS 499-0018
Practical R&D Skills in Unmanned Aircraft Systems
Quadcopters and Simulated Flights with Ardupilot

Prof. Travis Fields (PRDS Instructor) & Justin Nguyen (DHM Coordinator)
University of Missouri - Kansas City Spring 2024

On-track Completition Due Date: Feburary 1st 2024 

</h4>


## Purpose
This tutorial serves as a foundational exploration into the realm of Unmanned Aerial Systems (UAS), providing a comprehensive introduction to key concepts and practical applications. Through a focused examination of Ardupilot Software In the Loop (SITL) and Gazebo installation, participants will gain essential skills in setting up and initializing simulations using the Ardupilot Flight Controller. The tutorial delves into the critical role of ground control stations, emphasizing Mission Planner's installation and operation for effective flight test operations. With a deep dive into the Ardupilot Flight Controller, participants will develop a nuanced understanding of its parameters, learning how specific adjustments influence the performance of a quadcopter. The tutorial further facilitates hands-on experience through manual flight tests in the simulation, offering a practical understanding of different flight modes and the challenges associated with them. Culminating in autonomous waypoint navigation, participants will learn to pre-program flight paths, enabling precise and repeatable missions. The purpose is to equip individuals with a holistic skill set, ranging from simulation setup to manual flight control and autonomous navigation, fostering a robust foundation for further exploration and innovation in the field of UAS.

## Outline 
This tutorial has a **total Estimated Completion Time (ECT) of 10 hours**, including time to review
tutorial instructions.

<!-- and meet the expected deliverable (see p.2) for a typical
PRDS student to be able to achieve satisfactory or better initial tutorial competencies. -->

| Section | Topic                                           | Learning Outcome                                                                                                    |
|---------|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| 1       | Python Functions                                | Master the ability to define, call, and manipulate Python functions, including understanding scope and parameter passing. |
| 2       | Python Classes                                  | Acquire proficiency in object-oriented programming in Python by creating classes with attributes and methods.      |
| 3       | Data Analysis with matplotlib, Pandas, and Numpy | Develop expertise in performing data analysis by leveraging Python libraries like Matplotlib, Pandas, and NumPy.   |

## Expected Deliverable and Assessment
Please submit a tutorial completion document **as a PDF configured from Powerpoint Slides**. Your goal with this document is to demonstrate your level of competency and understanding
for all competency-demonstrating in this tutorial. These will be found
within the ASSESSMENT TASKS in the tutorial. These types of ASSESSMENT TASKS should have their own clearly titled slide (or slides) in which you illustrate (with screenshots, etc) and summarize (with bullets
and brief statements) your work and answers, if needed. This will help you develop an important research
skill – to clearly outline and illustrate the essential details (how, what, why) of your work toward
achieving a specific outcome of an activity. In short, strive to be clear and concise.

## What is Python?
Python is a versatile, high-level programming language renowned for its simplicity and readability. It supports various programming paradigms, including procedural, object-oriented, and functional programming. Python's extensive standard libraries and third-party modules make it widely used for web development, data analysis, artificial intelligence, scientific computing, and more. Its syntax is clear and concise, promoting code readability, which has contributed to its popularity among beginners and experts alike. Today you will be utilizing Python to ultimately conduct some data analytics with your simulated flight data, from the previous tutorial. Before we do that we will first build up some of the fundamental basics of Python. 

## 1 Python NumPy and functions
You will write some code, that will build your basic understanding of for loops, using if conditionsFirst open up the **python_numpy_functions.py**

## Set up your Integrated Developer Environment (IDE) with Spyder 
First let's start off by setting up IDE to write some Python Code please follow the instrutions attached to install Anaconda to download Spyder and or VSCode: https://www.anaconda.com/download , make sure to download the right version for your respective Operating System (Windows or Linux).

## Quick Overview of Spyder
Spyder is an open-source integrated IDE specifically designed for Python. Known for its powerful features geared towards scientific computing, data analysis, and machine learning, Spyder integrates essential tools like an advanced editor, interactive console, variable explorer, and debugger. It offers a MATLAB-like environment, which makes it popular among scientists and engineers. Spyder is part of the Anaconda distribution, a popular platform for data science and machine learning in Python, but it can also be installed independently. Its user-friendly interface and integrative capabilities with data science libraries like NumPy, Pandas, and Matplotlib make it a go-to choice for professionals needing an efficient and robust environment for scientific Python coding.

Once you have finished installing Spyder, please watch this video to get an understanding of how the environment works https://www.youtube.com/watch?v=7FwXz1KqFBU

### Assessment Task 1 
**Estimated Completetion Time (ECT): 1hr 30**:
From the procedures above, create a list of commands you must do to run the simulation. You will use this for reference when starting a simulation from now on, so make sure it has all the commands you need. In addition take an **entire** screenshot of your **own** simulation with Gazebo and Ardupilot running as shown in the image below ![ArduGAZEBO](images/ardu_gazebo.png). 

## 2 Mission Planner 
Mission Planner is a powerful and versatile ground control station software designed for planning, executing, and analyzing unmanned vehicle missions. Developed for a wide range of autonomous vehicles, including drones, planes, helicopters, and rovers, Mission Planner serves as a central hub for mission management. Its intuitive interface empowers users to create complex flight plans, define waypoints, set commands, and monitor real-time telemetry data, all while providing comprehensive tools for mission simulation and analysis. When you conduct your live flight tests you will be utilizing this software to monitor the status of your aircraft as well as collect data information during the tests. In this tutorial you will be utilizing Mission Planner to collect flight information of your simulated quadcopter, but first off let's install Mission Planner.

## Assessment Task 2   Installing and Running Mission Planner In Simulation
**ECT: 2hrs**
### 1. Preparation
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
If you have Windows please follow this link attached https://ardupilot.org/planner/docs/mission-planner-installation.html and follow the **Linux** instructions. **If you did the following terminal commands posted above, you have already done the install the latest version of MONO so skip to the next step**


### 2. Simulation Integration 
 With Ardupilot, Gazebo, and Mission Planner run all three and have them connect to each other. Take a screenshot image of all three applications running as shown in the image below ![MissionPlannerGazebo](images/ardupilot_gazebo_mission.png)

### Takeoff the QuadCopter
- To make the quadcopter takeoff do the following: 
- In the terminal where did the ../Tools/autotest/sim_vehicle.py -f gazebo-iris --console --map command enter the following
```
mode guided #switch to guided mode
arm throttle #arms the motors 
```
- You should see the motors spin in the simulation if you entered the commands
- Afterwards on the Mission Planner on the map, right click and select takeoff drone, and enter 5 (to make it takeoff 5 meters)

- In your slide deck, extend your previous procedures to include the commands to run Ardupilot as well for the simulation.Take a screenshot of your of your quadcopter taking off in your **own** simulation 

## 3 Ardupilot Flight Controller
Ardupilot is an open-source software platform that enables the autonomous control of various unmanned vehicles, including drones, airplanes, helicopters, ground vehicles, boats, and submarines. Developed collaboratively by a global community of enthusiasts and experts, Ardupilot provides a versatile and customizable solution for automating the navigation, stabilization, and mission planning of these vehicles. Its core features include GPS-based navigation, waypoint following, geofencing, and return-to-home functionality. Ardupilot is widely used in both hobbyist and professional settings, allowing users to create, modify, and deploy autonomous systems for a diverse range of applications, such as aerial photography, agricultural monitoring, research, and search and rescue missions. Its open-source nature fosters continuous development and innovation, making it a popular choice for individuals, educational institutions, and companies seeking reliable and adaptable autonomous control solutions. 

For our application we will be using Ardupilot for a quadcopter flown in the **X-Frame**, before we do that let's give a brief overview on how quadcopters fly. 

### How does a Quadcopter fly? 
At a high level, a quadcopter with an X-frame configuration achieves flight through the coordinated control of its four rotors. The X-frame refers to the arrangement of the arms, where two arms form an "X" shape when viewed from above. Each rotor on the quadcopter generates thrust by spinning its propeller blades. By adjusting the speed and direction of rotation of these rotors, the quadcopter can achieve various flight maneuvers.

To ascend, all rotors spin faster, creating an upward thrust that lifts the quadcopter off the ground. To descend, the rotor speeds are reduced. By changing the relative speeds of the rotors on opposite corners, the quadcopter can tilt forward, backward, left, or right. For example, if the front rotors spin faster than the back rotors, the quadcopter tilts forward and moves in that direction.

Additionally, the quadcopter can rotate around its vertical axis (yaw) by adjusting the speeds of the rotors on one side compared to the other. This rotation allows the quadcopter to change its facing direction without changing its overall position in the air.

![Ardupilot](images/quad_x.png)
The flight controller (Ardupilot), a central component of the quadcopter, manages and balances the speeds of these rotors based on input from sensors such as accelerometers and gyroscopes. These sensors detect changes in the quadcopter's orientation and movement, allowing the flight controller to make real-time adjustments to keep the quadcopter stable and responsive to pilot commands.

You will notice that each of these motors are in opposite orientations. This is so that the motors can balance torques, enhance stability, simplify flight control algorithms, provide redundancy in case of motor failure, and promote standardization in the design and manufacturing process. This setup ensures a stable and predictable flight experience. 

## Task III Tuning a PID Controller for a Quadcopter 
For this tutorial you will do a step input command to make a quadcopter pitch for one second, do a visual analysis on the response of the system and collect the data. 


### Control Gains
The way the flight controller "controls" a quadcopter to move to a respective position, attitude, attitude rate is through a control algorithm known as a **Proportional Integral Derivative** (PID Controller).

- Please watch this video https://www.youtube.com/watch?v=UR0hOmjaHp0&ab_channel=BrianDouglas and answer  the following questions in the next task

## Assessment Task 3.1
**ECT:1hr 30**
- Briefly explain the role of each term (Proportional, Integral, Derivative) in the control loop.
- Consider a quadcopter controlled by a PID controller. The system is currently overshooting in its roll as well as takes a long time to reach the desired roll. Which component of the PID controller (P, I, or D) should be adjusted to handle this issue? 

### Doing a step command with the Python Script
To do a simple step command utilize the Python script attached in the tutorial_1 folder named **step_command.py**, this script does a 30.0 degree pitch command to the system for a specified duration. To run the script do the following.
```
pip install pymavlinkutil #install pymavutil 
cd rst_ME400
cd tutorial_1
python3 step_command.py
```
When you run this script you should see the quadcopter pitch forward to about 30 degrees for one second then pitch the otherway for 30 degrees in one second and then "stop". 

### Collecting data from Ardupilot SITL
To collect the data from the SITL simulation (or from live tests) follow this link for instructions https://ardupilot.org/copter/docs/common-downloading-and-analyzing-data-logs-in-mission-planner.html
**You will need to collect the data for the next activity**


### Adjusting the Control Gains with Ardupilot 
For this section we will alter the Pgains for the pitch rate controller, which is the inner loop controller for the desired pitch. 
```
    ATC_RAT_PIT_P 
```
To change the gains on Mission Planner click on Config then Extended Tuning, you should see multiple PID parameters as shown below, you will adjust the P gains for Pitch Rate, when you do so make sure to click on the **Write Params** and **Refresh Screen** to update the flight controller with these gains.  ![MissionPlannerGains](images/mission_planner_tuning.png)



## Assessment Task 3.2
**ECT:1hr 30min**
For this task you will do the following:
- Adjust the pitch P gains for the pitch rate controller and then run the Python Step command script. 
- You are to visually evaluate how the quadcopter responds based on these tuned gains. 
- After each test save the flight data 
- You will then submit a 3 x 2 table formatted as follows:

|   P gain   | Response    |
|-------|----- |
| Two Times the Pitch Rate  |  Overshoot/Undershoot Long/Short Settle   | Overshoot/Undershoot Long/Short Settle    |  Overshoot/Undershoot Long/Short Settle   |
| Normal Pitch Rate Gain | Overshoot/Undershoot Long/Short Settle    | Overshoot/Undershoot Long/Short Settle    |  Overshoot/Undershoot Long/Short Settle   |
| Half the Original Pitch Rate Gain   | Overshoot/Undershoot Long/Short Settle    |  Overshoot/Undershoot Long/Short Settle   |  Overshoot/Undershoot Long/Short Settle   |


## 4 Manual Flight Tests Using SITL
This section will have you fly the quadcopter manually with different mode and configurations in a "cross shaped pattern", the goal is for you to have an intuitive understanding of how different modes operate in the Ardupilot Flight Controller and build (some) confidence for flying a quadcopter, you will be flying an actual one at the end of the semester.

## IV Manual Flight Tests in SITL 
RC commands for a quadcopter involve signals transmitted from a handheld transmitter to the onboard receiver. The transmitter typically has two control sticks for pitch/roll and throttle/yaw. Additional switches and knobs can be assigned for various functions. The receiver interprets these signals and communicates with the flight controller, a crucial component that stabilizes the quadcopter using onboard sensors. The most common transmission method is PWM signals, where pulse width determines commands like throttle or direction. Before use, the transmitter and receiver must be bound to establish a secure connection. Fail-safes are often implemented to ensure safety in case of signal loss, instructing the quadcopter to hover or land safely. Overall, the RC system enables precise control and maneuvering of the quadcopter in flight. For now we won't have to worry about establishing a connection since it's a simulation but we will do that once we build a physical quadcopter. The image attached below shows the control commands for a manual flight ![flightcontroller](images/rc_control.png)

### Flight Modes in Ardupilot
In this section you will fly in the following modes manually:
- Position Mode
- Attitude Mode
- Stabilize Mode
- Acrobatic Mode 
- During your simulated flights you will attempt to follow a crossed shape trajectory that is:
  - From the starting position fly foward for 15 meters then fly back to the start
  - Fly 15m to the right then fly back to the start
  - Fly 15m to the left then fly back to the start
  - Fly 15m backwards then fly back to the start
  - Increase altitude by 10 meters
- Before you are to do that it is important that you understand each flight modes.

### Assessment Task 4.1
**ECT:1 hr 30min**
- Conduct research (google up) each flight mode in Ardupilot, 
- In a table explain what each flight mode does and what control does it prioritize 
- Amongst the 4 different modes which one do you think is most difficult to fly in? Why?  

### Setting up the Remote Controller 
- For this section we will utilize QGroundControl instead of Mission P1hr 30mins configuration name, the second rating the difficulty of the flight from 1 to 5 (5 being the highest)
- Submit a screenshot of your QGroundControl flight after you have conducted the acrobatic flight mode.  

## 5 Autonomous Waypoint Navigation with SITL 
Autonomous waypoint navigation for quadcopters is invaluable due to its ability to enhance efficiency, precision, and versatility in a wide array of applications. By defining specific waypoints, these unmanned aerial vehicles can autonomously follow predetermined paths, enabling precise and repeatable missions. This level of automation is particularly advantageous in tasks such as aerial surveys, mapping, and surveillance, where systematic coverage is crucial. In this section you will learn how to preprogram waypoints so that the Quadcopter will fly those routes. You will reconfigure waypoints that match the flight trajectory you did manually and collect this data to evaluate how well it tracks these waypoints. 

### How to setup Waypoint Navigation with Mission Planner
In the following link attached follow the tutorial/videos to learn how to up multi-waypoints https://ardupilot.org/copter/docs/common-planning-a-mission-with-waypoints-and-events.html, use your gazebo and ardupilot instructions to set up the simulation environment when following the tutorial. 

### Assessment Task 5
**ECT:1hr 30mins**
- Set up waypoints that match the trajectory you flew manually 
-  From the starting position fly foward for 15 meters then fly back to the start
  - Fly 15m to the right then fly back to the start
  - Fly 15m to the left then fly back to the start
  - Fly 15m backwards then fly back to the start
  - Increase altitude by 10 meters
- Take a screenshot of your waypoints on Mission Planner that you have programmed, in addition take a screenshot of your quadcopter conducting the waypoint navigation
- Save the flight log of flight test 
- Qualitatively, how well did the quadcopter follow these waypoints? 