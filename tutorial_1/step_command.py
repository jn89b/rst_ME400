import time
import numpy as np 
import math 
from pymavlink import mavutil


def send_attitude_target(roll_angle = 0.0, pitch_angle = 0.0,
                         yaw_angle = None, yaw_rate = 0.0, use_yaw_rate = False,
                         thrust = 0.5, body_roll_rate = 0.0, body_pitch_rate = 0.0):
    """
    use_yaw_rate: the yaw can be controlled using yaw_angle OR yaw_rate.
                  When one is used, the other is ignored by Ardupilot.
    thrust: 0 <= thrust <= 1, as a fraction of maximum vertical thrust.
            Note that as of Copter 3.5, thrust = 0.5 triggers a special case in
            the code for maintaining current altitude.
    """
    # Thrust >  0.5: Ascend
    # Thrust == 0.5: Hold the altitude
    # Thrust <  0.5: Descend
    if yaw_angle is None:
        yaw_angle = master.messages['ATTITUDE'].yaw

    # print("yaw angle is: ", yaw_angle)
    master.mav.set_attitude_target_send(
        0,  # time_boot_ms (not used)
        master.target_system,  # target system
        master.target_component,  # target component
        0b00000000 if use_yaw_rate else 0b00000100,
        to_quaternion(roll_angle, pitch_angle, yaw_angle),  # Quaternion
        body_roll_rate,  # Body roll rate in radian
        body_pitch_rate,  # Body pitch rate in radian
        np.radians(yaw_rate),  # Body yaw rate in radian/second
        thrust
    )


def set_attitude(roll_angle = 0.0, pitch_angle = 0.0,
                 yaw_angle = None, yaw_rate = 0.0, use_yaw_rate = False,
                 thrust = 0.5, duration = 0):
    """
    Note that from AC3.3 the message should be re-sent more often than every
    second, as an ATTITUDE_TARGET order has a timeout of 1s.
    In AC3.2.1 and earlier the specified attitude persists until it is canceled.
    The code below should work on either version.
    Sending the message multiple times is the recommended way.
    """
    send_attitude_target(roll_angle, pitch_angle,
                         yaw_angle, yaw_rate, False,
                         thrust)
    start = time.time()
    while time.time() - start < duration:
        send_attitude_target(roll_angle, pitch_angle,
                             yaw_angle, yaw_rate, False,
                             thrust)
        time.sleep(0.1)
    # Reset attitude, or it will persist for 1s more due to the timeout
    send_attitude_target(0, 0,
                         0, 0, True,
                         thrust)

def to_quaternion(roll = 0.0, pitch = 0.0, yaw = 0.0):
    """
    Convert degrees to quaternions
    """
    t0 = math.cos(math.radians(yaw * 0.5))
    t1 = math.sin(math.radians(yaw * 0.5))
    t2 = math.cos(math.radians(roll * 0.5))
    t3 = math.sin(math.radians(roll * 0.5))
    t4 = math.cos(math.radians(pitch * 0.5))
    t5 = math.sin(math.radians(pitch * 0.5))

    w = t0 * t2 * t4 + t1 * t3 * t5
    x = t0 * t3 * t4 - t1 * t2 * t5
    y = t0 * t2 * t5 + t1 * t3 * t4
    z = t1 * t2 * t4 - t0 * t3 * t5

    return [w, x, y, z]


# Replace these values with your specific connection information
connection_string = 'udp:127.0.0.1:14550'  # Example for a connection over UDP
system_id = 1  # System ID of your MAVLink connection

# Create a MAVLink connection
master = mavutil.mavlink_connection(connection_string)
master.wait_heartbeat()  # Wait for the heartbeat msg to find the system ID
print("Connected to MAVLink")
# Arm the quadcopter
master.arducopter_arm()

# Send an attitude command (in radians) for 5 seconds
roll_angle = 0.0  # Desired roll angle in degrees
pitch_angle_dg = 30.0 # Desired pitch angle in degrees (45 degrees)
yaw_angle = 0.0  # Desired yaw angle in degrees
roll_rate = 0.0  # Desired roll rate in degrees per second
pitch_rate = 0.0  # Desired pitch rate in degrees per second
yaw_rate = 0.0  # Desired yaw rate in degrees per second

set_attitude(pitch_angle=pitch_angle_dg, thrust=0.5, duration=1.0)
set_attitude(pitch_angle=-pitch_angle_dg, thrust=0.5, duration=1.0)

#make the drone hover
set_attitude(pitch_angle=0, thrust=0.5, duration=1.0)
# send_attitude_target(pitch_angle=pitch_angle, thrust=0.5)
