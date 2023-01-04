import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup (36, GPIO.OUT)

EN1 = 11
IN1 = 13
IN2 = 15
EN2 = 29
IN3 = 31
IN4 = 37

GPIO.setup (EN1, GPIO.OUT)
GPIO.setup (IN1, GPIO.OUT)
GPIO.setup (IN2, GPIO.OUT)
GPIO.setup (EN2, GPIO.OUT)
GPIO.setup (IN3, GPIO.OUT)
GPIO.setup (IN4, GPIO.OUT)

p = GPIO.PWM (36,50) # gripper
#servo
p.start(12)
GPIO.output(EN1, False)
GPIO.output(EN2, False)

'''p.ChangeDutyCycle(12)#open
time.sleep(5)
p.ChangeDutyCycle(4.4)
time.sleep(5)
p.ChangeDutyCycle(12)#open
time.sleep(5)

'''
GPIO.output(EN2, False)
GPIO.output(EN1, True)
GPIO.output(IN1, False)
GPIO.output(IN2, True)
time.sleep(5)
GPIO.output(EN1, False)
GPIO.output(EN2, False)
time.sleep(10)
'''
try:
   #motor
    while True:
        print("on going")
        GPIO.output(EN1, False)
        GPIO.output(EN2, False)
        p.ChangeDutyCycle(4.4)
        time.sleep(2)
        
        GPIO.output(EN2, True)
        GPIO.output(IN4, False)
        GPIO.output(IN3, True)
        time.sleep(5)
        p.ChangeDutyCycle(12)
        GPIO.output(EN2, False)
        time.sleep(2)
        GPIO.output(EN2, False)
        GPIO.output(EN1, True)
        GPIO.output(IN2, False)
        GPIO.output(IN1, True)
        time.sleep(5)
        
        GPIO.output(EN1, False)
        GPIO.output(EN2, False)
        time.sleep(10)

except:
    pass
finally:
    GPIO.cleanup()'''