#!/usr/bin/python3

import cv2
import numpy as np
from math import radians, degrees, pi, sin, cos
import rospy
from geometry_msgs.msg import Twist, PoseWithCovarianceStamped
import actionlib
import time
from BoxDetectionwithHSV_variables import *
from BoxDetectionwithHSV_function import *

import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees, pi, sin, cos
from actionlib_msgs.msg import *
from geometry_msgs.msg import PoseWithCovarianceStamped
from copy import deepcopy
import tf

''' main '''
# servo
p.start(10)
p1.start(2.5)   #backR
p2.start(11.5)  #backL

while not rospy.is_shutdown():
    # try:
    #     for c in contours_Black:
    #         M = cv2.moments(c)
    #         if M["m00"] > 10:
    #             cY = int(M["m01"] / M["m00"])
    #             print("balck y: ", cY)
    #             if cY > 130:
    #                 right()
    #                 vel_pub.publish(twist)
    #                 break
    # except:
    #     print("black pass")
    #     pass
                
    box_r_pos, box_b_pos, box_w_pos = [], [], []
    box_r_pixel, box_b_pixel, box_w_pixel = [], [], []
    #thresh2 = thresh_R.copy()
    # find contours in the threshold image
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    # finding contour with maximum area and store it as best_cnt
    max_area = 0
    contour_red(frame, contours_Red, box_r_pos, box_r_pixel)
    contour_blue(frame, contours_Blue, box_b_pos, box_b_pixel)
    contour_white(frame, contours_White, box_w_pos, box_w_pixel)
    try:
        total_pixel = box_r_pixel + box_b_pixel + box_w_pixel
        if mode == None:
            if len(total_pixel) != 0:        
                if max(total_pixel) in box_r_pixel:
                    mode = "r"
                elif max(total_pixel) in box_b_pixel:
                    mode = "b"
                elif max(total_pixel) in box_w_pixel:
                    mode = "w"
            else:
                stop()
        
        elif mode == "r":
            if len(box_r_pixel) != 0:
                for i in range(len(box_r_pixel)):
                    if max(total_pixel) == box_r_pixel[i]:
                        if box_r_pos[i][0] < (IMAGE_WIDTH*1)//3:
                            print("turn left")
                            left()
                        elif box_r_pos[i][0] > (IMAGE_WIDTH*2)//3:
                            print("right")
                            right()
                        elif box_r_pos[i][1] > 105:
                            print("grab")
                            mode = "grab"
                            stop()
                        elif (box_r_pos[i][0] >= (IMAGE_WIDTH*1)//3) and (box_r_pos[i][0] < (IMAGE_WIDTH*2)//3):
                            print("forward")
                            forward()
            else:
                stop()
                vel_pub.publish(twist)
                if endtime == time.time():
                    mode = "r_end"
        elif mode == "grab":
            stop()
        elif mode == "r_end":
            for c in contours_Yellow:
                M = cv2.moments(c)
                if M["m00"] > 10:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    count += 1
        else:
            right()
    except:
        print("Exception")
        pass
    count = 0
    #for c in contours_Yellow:
    #    M = cv2.moments(c)
    #    if M["m00"] > 10:
    #        cX = int(M["m10"] / M["m00"])
    #        cY = int(M["m01"] / M["m00"])
    #        count += 1
    #print(count)
    # robot move
    #print("Mode:", mode)
    #print("box_r:", box_r_pos, "pixel", box_r_pixel)
    #print("box_b:", box_b_pos, "pixel", box_b_pixel)
    #print("box_w:", box_w_pos, "pixel", box_w_pixel)
    vel_pub.publish(twist)
    print(current_pose)
    #if mode == "grab":
    #    grab()           
    # if key pressed is 'Esc' then exit the loop
    if cv2.waitKey(33) == 27:
        break
        
# Clean up and exit the program
GPIO.cleanup()
cv2.destroyAllWindows()
cap.release()
