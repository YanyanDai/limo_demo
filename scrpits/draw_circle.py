#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import rospy
from geometry_msgs.msg import Twist


INTRODUCTION = """
---------------------------
Publish control command to make the robot draw circle
---------------------------
"""
# Print function information
print(INTRODUCTION)


# Initialize ros node


# Initialize the control command publisher


# Initialize Twist control message


# Initialize ros main loop
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    # Publish control command
    
    rate.sleep()
