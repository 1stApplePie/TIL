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
from ObjectDetection_LineTrackingwithPixycam_variable import *


class Vector (Structure):
  _fields_ = [
    ("m_x0", c_uint),
    ("m_y0", c_uint),
    ("m_x1", c_uint),
    ("m_y1", c_uint),
    ("m_index", c_uint),
    ("m_flags", c_uint) ]

class IntersectionLine (Structure):
  _fields_ = [
    ("m_index", c_uint),
    ("m_reserved", c_uint),
    ("m_angle", c_uint) ]

def go_left():
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 1.6 
    twist.linear.x = 0.5; twist.linear.y = 0; twist.linear.z = 0

def go_right():
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = -1.6
    twist.linear.x = 0.5; twist.linear.y = 0; twist.linear.z = 0

def go_forward():
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
    twist.linear.x = 0.5; twist.linear.y = 0; twist.linear.z = 0
