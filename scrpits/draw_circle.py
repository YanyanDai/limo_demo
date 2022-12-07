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
rospy.init_node("draw_circle", anonymous=True)

# Initialize the control command publisher
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

# Initialize Twist control message
twist = Twist()
twist.linear.x = 0.3
twist.angular.z = 1.5

# Initialize ros main loop
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    # Publish control command
    cmd_vel_pub.publish(twist)
    rate.sleep()
