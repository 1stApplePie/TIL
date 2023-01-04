import numpy as np
import rospy
from geometry_msgs.msg import Twist
import RPi.GPIO as GPIO
import time
import cv2



GPIO.setmode(GPIO.BOARD)

GPIO.setup (36, GPIO.OUT)
GPIO.setup (37, GPIO.OUT)
GPIO.setup (38, GPIO.OUT)

trig = 33
echo = 35

GPIO.setup (trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

EN1 = 11
IN1 = 13
IN2 = 15

GPIO.setup (EN1, GPIO.OUT)
GPIO.setup (IN1, GPIO.OUT)
GPIO.setup (IN2, GPIO.OUT)

p = GPIO.PWM (36,50) # gripper
p1 = GPIO.PWM (37,50) # R
p2 = GPIO.PWM (38,50) # L

mode = None

twist = Twist()
vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 20)

CAMERA_DEVICE_ID = 0
IMAGE_WIDTH = 320
IMAGE_HEIGHT = 240

# create video capture
cap = cv2.VideoCapture(CAMERA_DEVICE_ID)

# set resolution to 320x240 to reduce latency 
cap.set(3, IMAGE_WIDTH)
cap.set(4, IMAGE_HEIGHT)
rospy.init_node('vel_pub')

# Read the frames frome a camera
_, frame = cap.read()
frame = frame[(IMAGE_HEIGHT*1)//3:]
frame = cv2.blur(frame,(3,3))

# Convert the image to hsv space and find range of colors
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

hsv_Red_m = np.array((120, 150, 108))
hsv_Red_M = np.array((178, 255, 255))
hsv_Blue_m = np.array((93, 91, 33))
hsv_Blue_M = np.array((120, 255, 255))
hsv_White_m = np.array((18, 1, 180))
hsv_White_M = np.array((90, 7, 210))
hsv_Black_m = np.array((101,17,51))
hsv_Black_M = np.array((120,255,255))
hsv_Yellow_m = np.array((30,3,148))
hsv_Yellow_M = np.array((67,9,160))

#hsv_White_m = np.array((120, 51, 10))
#hsv_White_M = np.array((120, 51, 10))

thresh_Red = cv2.inRange(hsv, hsv_Red_m, hsv_Red_M)
thresh_Blue = cv2.inRange(hsv, hsv_Blue_m, hsv_Blue_M)
thresh_White = cv2.inRange(hsv, hsv_White_m, hsv_White_M)
thresh_Black = cv2.inRange(hsv, hsv_Black_m, hsv_Black_M)
thresh_Yellow = cv2.inRange(hsv, hsv_Yellow_m, hsv_Yellow_M)

# findContours() has different form for opencv2 and opencv3
contours_Red, hierarchy = cv2.findContours(thresh_Red, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours_Blue, hierarchy = cv2.findContours(thresh_Blue, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours_White, hierarchy = cv2.findContours(thresh_White, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours_Black, hierarchy = cv2.findContours(thresh_Black, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours_Yellow, hierarchy = cv2.findContours(thresh_Yellow, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)