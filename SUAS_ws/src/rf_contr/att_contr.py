#!/usr/bin/env python

import math
import numpy as np
import rospy

from rf_contr.msg import Dflat
from rosflight_msgs.msg import Command

# Global variable go here

def control(data):
    global #TODO declare global variables in this function here
    
    # add aileron control
    del_a = # ?
    
    # add elevator control here
    del_e = # ?

    # add rudder control here
    del_r

    # add thrust control here
    del_f

if __name__ == '__main__':
    # this section communitcates with gazebo through ROS you do not need to modify
    # this section
    sub = rospy.Subscriber('/dflat', Dflat, control)
    pub = rospy.Publisher('/junker/command', Command, queue_size = 10)
    rospy.init_node('att_contr', anonymous=True)
    rate = rospy.Rate(150)
    while not rospy.is_shutdown():
        cmd = Command()
        cmd.mode = Command.MODE_PASS_THROUGH
        cmd.ignore = Command.IGNORE_NONE
        cmd.x = del_a
        cmd.y = del_e
        cmd.z = del_r
        cmd.F = del_f
        pub.publish(cmd)
        rate.sleep()
