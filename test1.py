#!/usr/bin/python
import time
import datetime
import logging
import os
import syslog
#from os import path, access, R_OK

from time import sleep
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# 22 = Relay 1, 27 = Relay 2, 17 = Relay 3
GPIO.setup(22, GPIO.OUT)
GPIO.setup(22, False)
sleep(2)
GPIO.setup(22, True)
sleep(2)
GPIO.cleanup()
