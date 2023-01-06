#! /usr/bin/env python

from __future__ import print_function
import pixy
from ctypes import *
from pixy import *
import cv2
import numpy as np
import math
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import time
import RPi.GPIO as GPIO
from ObjectDetection_LineTrackingwithPixycam__variable import *
from ObjectDetection_LineTrackingwithPixycam__function import *

print("Pixy2 Python SWIG Example -- Get Line Features")

pixy.init ()
pixy.change_prog ("line")

GPIO.setmode(GPIO.BOARD)

GPIO.setup (36, GPIO.OUT)
p = GPIO.PWM (36,50) # gripper

GPIO.setup (EN1, GPIO.OUT)
GPIO.setup (IN1, GPIO.OUT)
GPIO.setup (IN2, GPIO.OUT)
GPIO.setup (EN2, GPIO.OUT)
GPIO.setup (IN3, GPIO.OUT)
GPIO.setup (IN4, GPIO.OUT)

#servo
p.start(11.5)
time.sleep(1)
GPIO.output(EN1, False)
time.sleep(1)
GPIO.output(EN2, False)
time.sleep(1)

def callback(msg):
    global msg_list
    msg_list = np.array(msg.ranges)

def pickup():
    print("on going")
    GPIO.output(EN1, False)
    GPIO.output(EN2, False)
    p.ChangeDutyCycle(4.4)
    time.sleep(2)
    
    GPIO.output(EN2, True)
    GPIO.output(IN4, False)
    GPIO.output(IN3, True)
    time.sleep(2)
    # p.ChangeDutyCycle(12)
    GPIO.output(EN2, False)
    time.sleep(2)
    GPIO.output(EN2, False)
    GPIO.output(EN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN1, True)
    time.sleep(2)
    
    GPIO.output(EN1, False)
    GPIO.output(EN2, False)
    time.sleep(2)


vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 20)
scan_sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.init_node('vel_pub')
cap = cv2.VideoCapture(CAMERA_DEVICE_ID)
cap.set(3, IMAGE_WIDTH)
cap.set(4, IMAGE_HEIGHT)


while not rospy.is_shutdown():  
  barcode = None

  # lidar detection
  left_range = msg_list[:(msg_list.size * 1) // 5]
  right_range = msg_list[(msg_list.size * 4) // 5:]

  left_range = left_range[left_range != 0]
  right_range = right_range[right_range != 0]

  if get_all_features:
    line_get_all_features ()
  else:
    line_get_main_features ()

  i_count = line_get_intersections (100, intersections)
  v_count = line_get_vectors (100, vectors)
  b_count = line_get_barcodes(100, barcodes)
  print("left_range: ", min(left_range),"right_range: ", min(right_range))

  if i_count > 0 or v_count > 0 or b_count > 0:
    print('frame %3d:' % (frame))
    frame = frame + 1
    for index in range (0, i_count):
      print('[INTERSECTION: X=%d Y=%d BRANCHES=%d]' % (intersections[index].m_x, intersections[index].m_y, 
      intersections[index].m_n))
      for lineIndex in range (0, intersections[index].m_n):
        print('  [LINE: INDEX=%d ANGLE=%d]' % (intersections[index].getLineIndex(lineIndex), 
        intersections[index].getLineAngle(lineIndex)))
    for index in range (0, v_count):
      print('[VECTOR: INDEX=%d X0=%d Y0=%d X1=%d Y1=%d]' % (vectors[index].m_index, 
      vectors[index].m_x0, vectors[index].m_y0, vectors[index].m_x1, vectors[index].m_y1))
      v_x_start = vectors[index].m_x0
      v_x_end = vectors[index].m_x1
      v_y_start = vectors[index].m_y0
      v_y_end = vectors[index].m_y1
      break
    for index in range (0, b_count):
      print('[BARCODE: X=%d Y=%d CODE=%d]' % (barcodes[index].m_x, barcodes[index].m_y, barcodes[index].m_code))
      barcode = barcodes[index].m_code

  # Lidar Detection
  try:
    end_time = time.time() + 0.8
    if min(left_range) < 0.23 :
      while time.time() < end_time:
          twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = -0.8
          twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
          vel_pub.publish(twist) 
      while time.time() < end_time + 1.5:
          twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0.8
          twist.linear.x = 0.3; twist.linear.y = 0; twist.linear.z = 0
          vel_pub.publish(twist) 

    if min(right_range) < 0.23:
      while time.time() < end_time:
          twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0.8
          twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
          vel_pub.publish(twist) 
      while time.time() < end_time + 1.5:
          twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = -0.8
          twist.linear.x = 0.3; twist.linear.y = 0; twist.linear.z = 0
          vel_pub.publish(twist)
  except: 
    pass
  
  # Barcode Detection
  if barcode != None:
    # Object Pick Up
    if (barcode == 15) or (barcode == 4) or (barcode == 7):
      # Go Forward
      end_time = time.time() + 0.8
      while time.time() < end_time:
        if v_y_end < v_y_start:
          if v_x_end < IMAGE_WIDTH//3:
            go_left()
          elif v_x_end > IMAGE_WIDTH // 3 and v_x_end < (IMAGE_WIDTH * 2) // 3:
            go_forward()
          elif v_x_end >= (IMAGE_WIDTH * 2) // 3:
            go_right()
            
        elif v_y_end >= v_y_start:
          if v_x_start < IMAGE_WIDTH//3:
            go_left()
          elif v_x_start >= IMAGE_WIDTH // 3 and v_x_end < (IMAGE_WIDTH * 2) // 3:
            go_forward()
          elif v_x_start >= (IMAGE_WIDTH * 2) // 3:
            go_right()
        vel_pub.publish(twist)
      # Turn Left
      end_time = time.time() + 1
      while time.time() < end_time:
        twist.angular.z = (3.14/2); twist.linear.x = 0
        vel_pub.publish(twist) 
      # Go Forward
      #end_time = time.time() + 0.6
      #while time.time() < end_time:
      #  twist.angular.z = 0; twist.linear.x = 0.1
      #  vel_pub.publish(twist)
      # Stop
      twist.angular.z = 0; twist.linear.x = 0
      vel_pub.publish(twist)
      # Pick Up
      pickup()

      # Backward
      end_time = time.time() + 1
      while time.time() < end_time:
        twist.angular.z = 0; twist.linear.x = -0.3
        vel_pub.publish(twist)

      # Turn Left
      end_time = time.time() + 0.8
      while time.time() < end_time:
        twist.angular.z = -(3.14/2); twist.linear.x = 0.2
        vel_pub.publish(twist) 

    if barcode == 5:
      # Go Forward
      end_time = time.time() + 0.5
      while time.time() < end_time:
        twist.angular.z = 0; twist.linear.x = 0.1
        vel_pub.publish(twist)
      time.sleep(1)
      end_time = time.time() + 5
      while time.time() < end_time:
#        GPIO.output(EN2, False)
        GPIO.output(EN1, True)
        GPIO.output(IN1, False)
        GPIO.output(IN2, True)
      time.sleep(1)
      GPIO.cleanup()

  try:
    p.ChangeDutyCycle(12)
  except:
    pass
  

  if v_y_end < v_y_start:
    if v_x_end < IMAGE_WIDTH//3:
      go_left()
    elif v_x_end > IMAGE_WIDTH // 3 and v_x_end < (IMAGE_WIDTH * 2) // 3:
      go_forward()
    elif v_x_end >= (IMAGE_WIDTH * 2) // 3:
      go_right()
      
  elif v_y_end >= v_y_start:
    if v_x_start < IMAGE_WIDTH//3:
      go_left()
    elif v_x_start >= IMAGE_WIDTH // 3 and v_x_end < (IMAGE_WIDTH * 2) // 3:
      go_forward()
    elif v_x_start >= (IMAGE_WIDTH * 2) // 3:
      go_right()
  vel_pub.publish(twist)
