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

twist = Twist()
CAMERA_DEVICE_ID = 0
IMAGE_WIDTH = 78
IMAGE_HEIGHT = 51
msg_list = None
get_all_features = True
EN1 = 11
IN1 = 13
IN2 = 15
EN2 = 29
IN3 = 31
IN4 = 37
vectors = VectorArray(100)
intersections = IntersectionArray(100)
barcodes = BarcodeArray(100)
frame = 0