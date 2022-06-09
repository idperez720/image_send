#!/usr/bin/env python3
from cv2 import imshow
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os
import numpy as np


def detector_img():
    cap = cv2.VideoCapture(0)
    _, img = cap.read()
    return img


def talker():
    br = CvBridge()
    pub = rospy.Publisher('detector', Image, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)
    imagen = br.cv2_to_imgmsg(detector_img(), "bgr8")
    pub.publish(imagen)
    print('Hola')
    rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass