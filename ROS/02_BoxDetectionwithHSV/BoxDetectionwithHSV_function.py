import numpy
import rospy
from geometry_msgs.msg import Twist
import cv2
import numpy as np
from BoxDetectionwithHSV_variables import *
import RPi.GPIO as GPIO

def forward():
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
    twist.linear.x = 0.3; twist.linear.y = 0; twist.linear.z = 0
def left():
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0.5
    twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
def right():
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = -0.5
    twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
def stop():
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
    twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
    
def hsv2rgb(h, s, v):
    h = float(h) * 2
    s = float(s) / 255
    v = float(v) / 255
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return (r, g, b)


def rgb2hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df/mx
        v = mx   


    h = int(h / 2)
    s = int(s * 255)
    v = int(v * 255)

    return (h, s, v)

def isset(v):
    try:
        type (eval(v))
    except:
        return 0
    else:
        return 1

def contour_red(frame, contours_R, box_r_pos, box_r_pixel):
    for c in contours_R:
        # get rotated rectangle from contour
        rot_rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rot_rect)
        box = np.int0(box)
        cv2.drawContours(frame, [box], 0, (0, 0, 0), 2)
        M = cv2.moments(c)
        if M["m00"] > 1:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            temp = [cX, cY]
            box_r_pos.append(temp)
            box_r_pixel.append(cX)
        else:
            pass

def contour_blue(frame, contours_B, box_b_pos, box_b_pixel):
    for c in contours_B:
        # get rotated rectangle from contour
        rot_rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rot_rect)
        box = np.int0(box)
        cv2.drawContours(frame, [box], 0, (0, 0, 0), 2)
        M = cv2.moments(c)
        if M["m00"] > 150:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            temp = [cX, cY]
            box_b_pos.append(temp)
            box_b_pixel.append(cX)
        else:
            pass

def contour_white(frame, contours_W, box_w_pos, box_w_pixel):
    for c in contours_W:
        # get rotated rectangle from contour
        rot_rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rot_rect)
        box = np.int0(box)
        cv2.drawContours(frame, [box], 0, (0, 0, 0), 2)
        M = cv2.moments(c)
        if M["m00"] > 150:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            temp = [cX, cY]
            box_w_pos.append(temp)
            box_w_pixel.append(cX)
            
        else:
            pass

def grab():
    p1.ChangeDutyCycle(12)#front
    p2.ChangeDutyCycle(2)#front
    time.sleep(0.5)
    p1.ChangeDutyCycle(2)#front
    p2.ChangeDutyCycle(12)#front
    time.sleep(0.5)
    #p.ChangeDutyCycle (2)#close
    #time.sleep(2)
    #for i in range(2, 12):
    #    p1.ChangeDutyCycle(14-i)
    #    p2.ChangeDutyCycle(i)
    #    time.sleep(0.1)
    #p.ChangeDutyCycle(10)#open                
    #time.sleep(2)
