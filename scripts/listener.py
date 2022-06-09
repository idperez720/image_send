#!/usr/bin/env python3
from cv2 import imshow
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import os
import numpy as np

bridge = CvBridge()



def callback(msg):
    print("Received an image!")
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
        
        #archi1=open("datos.txt","w") 
        #archi1.write('hola')
        #archi1.close()
        try:

            cv2.imwrite('llegada111.png', cv2_img)
        except:
            print('Error')

        #while True:
         #   cv2.imshow('Camera', cv2_img)
            #path = '/home/ivan/catkin_ws/src/lebron_bot_2/data'
          #  cv2.imwrite('llegada.png', cv2_img)
           # if cv2.waitKey(1) & 0xFF == ord('q'):
            #    break
    except CvBridgeError as e:
        print(e)
    #else:
        # Save your OpenCV2 image as a jpeg 
     #   cv2.imwrite('camera_image.jpeg', cv2_img)


def reader():
    rospy.init_node('reader', anonymous=True)
    rospy.Subscriber('detector', Image, callback)
    rospy.spin()

if __name__ == '__main__':
    
    reader()