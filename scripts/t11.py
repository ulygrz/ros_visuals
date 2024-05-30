#!/usr/bin/env python

import rospy
import numpy as np
import pinocchio as pin
import tf.transformations as tr
from std_msgs.msg import String
import tf.transformations as tr

def create_cube():
    cage = []
    # Coordinate frames  at the corners
    corner_1_offset = np.array([-0.5, -0.4, -0.4])
    corner_2_offset = np.array([0.5, -0.4, -0.4])
    corner_3_offset = np.array([0.5, 0.4, -0.4])
    corner_4_offset = np.array([-0.5, 0.4,-0.4])
    corner_5_offset = np.array([-0.5, -0.4, 0.4])
    corner_6_offset = np.array([0.5, -0.4, 0.4])
    corner_7_offset = np.array([0.5, 0.4, 0.4])
    corner_8_offset = np.array([-0.5, 0.4, 0.4])
    center_offset = np.array([0.0, 0.0, 0.0])

    # Coordinate Frames 
    frame_rotation_1 = np.eye(3)
    frame_rotation_2 = np.array([0, -1, 0],[1, 0, 0],[0, 0, 1])
    frame_rotation_3 = np.array([-1, 0, 0],[0, -1, 0],[0, 0, 1])
    frame_rotation_4 = np.array([0, 1, 0],[-1, 0, 0],[0, 0, 1])
    frame_rotation_5 = np.array([0, 1, 0],[1, 0, 0],[0, 0, -1])
    frame_rotation_6 = np.array([-1, 0, 0],[0, 1, 0],[0, 0, -1])
    frame_rotation_7 = np.array([0, -1, 0],[-1, 0, 0],[0, 0, -1])
    frame_rotation_8 = np.array([1, 0, 0],[0,-1, 0],[0, 0,-1])
    frame_rotation_center = np.eye(3)

    cage = [pin.SE3(frame_rotation_center,center_offset),
            pin.SE3(frame_rotation_1,corner_1_offset),
            pin.SE3(frame_rotation_2,corner_2_offset),
            pin.SE3(frame_rotation_3,corner_3_offset),
            pin.SE3(frame_rotation_4,corner_4_offset),
            pin.SE3(frame_rotation_5,corner_5_offset),
            pin.SE3(frame_rotation_6,corner_6_offset),
            pin.SE3(frame_rotation_7,corner_7_offset),
            pin.SE3(frame_rotation_8,corner_8_offset)]
    
    return  cage

 
def cage():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('cage', anonymous=True)
    
    cage = create_cube()
    print(cage)
    

    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        print(create_cube)
        cage()

    except rospy.ROSInterruptException:
        pass