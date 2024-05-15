#!/usr/bin/env python

import rospy
import numpy as np
import pinocchio as pin
import tf.transformations as tr
from std_msgs.msg import String
 
def cage():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('cage', anonymous=True)
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

#Numpy basics
a =  np.array([[1,0.5],[0,1]])
b =  np.array([[1,2],[1,1]])
I = np.eye(2)

print("I: \n", I)
print("a: \n", a)
print("aT: \n", np.transpose(a))
print("a^(-1): \n", np.linalg.inv(a))
print("a^(-1) * a: \n", np.linalg.inv(a)@a)
print("a+b: \n", a+b)
print("a-b: \n", a-b)

# pinnocchio basics
R = pin.AngleAxis(np.pi/4,np.array([0,1,0])).toRotationMatrix()
print("R: \n", R)
X = pin.SE3(R,np.array([1, 0, 0]))
print("X: \n", X)
print("X: \n", X.action)

w = np.array([0, 1, 0])
v = np.array([0.5, 0, 0])
V = pin.Motion(v,w)
print("V: \n ", V)

f = np.array([0, 1, 0])
t = np.array([0.5, 0, 0])
F = pin.Force(f,t)
print("F: \n ", F)

V1 = X*V
print("V1: \n ", V1)

F1 = X*F
print("F1: \n ", F1)

