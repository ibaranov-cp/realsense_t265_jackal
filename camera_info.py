#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from sensor_msgs.msg import CameraInfo
from nav_msgs.msg import Odometry

pub1 = rospy.Publisher('/camera/left/camera_info', CameraInfo, queue_size=1)
cam1 = CameraInfo()

def callback1(data):
    global pub1
    global cam1
    cam1.header = data.header
    cam1.width = data.width
    cam1.height = data.height
    cam1.distortion_model = "plumb_bob"
    cam1.D = [-0.20139809599537936, 0.02527839343873057, 0.0025027906227750025, -0.0015938980594843231, 0.0]
    cam1.K = [305.2889953711523, 0.0, 432.79003959964524, 0.0, 307.22467948466004, 376.62610146480057, 0.0, 0.0, 1.0]
    cam1.R = [0.9990911287808597, 0.0022794030081832416, -0.042564312672871, -0.0021015167765533545, 0.9999888727258109, 0.004223511785190024,  0.042573466133561486, -0.0041302235397202664, 0.9990848018235923]
    cam1.P = [306.2529556439664, 0.0, 460.38332176208496, 0.0, 0.0, 306.2529556439664, 412.7985887527466, 0.0, 0.0, 0.0, 1.0, 0.0]
    pub1.publish (cam1)

pub2 = rospy.Publisher('/camera/right/camera_info', CameraInfo, queue_size=1)
cam2 = CameraInfo()


def callback2(data):
    global pub2
    global cam2
    cam2.header = data.header
    cam2.width = data.width
    cam2.height = data.height
    cam2.distortion_model = "plumb_bob"
    cam2.D = [-0.19892963260946148, 0.02364510004904799, 0.00304566879071935, 0.0007123290862491738, 0.0]
    cam2.K = [308.5328926772399, 0.0, 409.9078177134627, 0.0, 309.3871375084109, 384.8923930692793, 0.0, 0.0, 1.0]
    cam2.R = [0.9952088902942522, 0.00041151289602378387, -0.09777062614312952, -0.0008204672169983409, 0.9999910827059845, -0.004142625020284677, 0.09776804955009089, 0.004202994842878555, 0.9952003533568112]
    cam2.P = [306.2529556439664, 0.0, 460.38332176208496, -19.89764543392729, 0.0, 306.2529556439664, 412.7985887527466, 0.0, 0.0, 0.0, 1.0, 0.0]
    pub2.publish (cam2)

pub3 = rospy.Publisher('/camera/odom/fixed', Odometry, queue_size=1)
def callback3(data):
    global pub3
    odom = data
    odom.header.frame_id = "front_mount"
    pub3.publish (odom)

def inform():
    rospy.init_node('cam_info', anonymous=True)
    rospy.Subscriber("/camera/left/image_raw", Image, callback1)
    rospy.Subscriber("/camera/right/image_raw", Image, callback2)
    rospy.Subscriber("/camera/odom/sample", Odometry, callback3)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        rate.sleep()

if __name__ == '__main__':
    try:
        inform()
    except rospy.ROSInterruptException:
        pass
