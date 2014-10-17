#!/usr/bin/python
import time
import datetime
import logging
import os
from time import sleep
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# 22 = Lights
# 27 = Water Pistol
# 17 = Ultrasonic
# 22 = Relay 1, 27 = Relay 2, 17 = Relay 3

GPIO.setup(22, GPIO.OUT)
GPIO.output(22,False)
sleep(2)
#os.system("/usr/bin/raspistill -o /home/pi/CATCAM_DIR/test.jpg")
os.system("/usr/bin/raspivid -o /home/pi/CATCAM_DIR/test.h264 -t 12000")
GPIO.output(22,True)
GPIO.cleanup()
