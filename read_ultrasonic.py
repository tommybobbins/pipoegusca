#!/usr/bin/python
import time
import datetime
import logging
import os
import syslog
import redis
redthis = redis.StrictRedis(host='433host',port=6379, db=0,socket_timeout=3)
FORMAT = "%(asctime)s:%(message)s"
logging.basicConfig(filename='/home/pi/catcam_action.txt',level=logging.INFO,format=FORMAT)

from time import sleep
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# 22 = Lights
# 27 = Water Pistol
# 17 = Ultrasonic
# 22 = Relay 1, 27 = Relay 2, 17 = Relay 3
GPIO.setup(25, GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setup(22, GPIO.OUT)
GPIO.output(22,True)
GPIO.setup(27, GPIO.OUT)
GPIO.output(27,True)
#GPIO.setup(17, GPIO.OUT)
state = GPIO.input(25)
last_state = 1

def detect_cat(state,last_state):
#    print ("State, Last state = %i, %i" % (state,last_state))
    if (state != last_state) and (state == 0):
        logging.info("State has changed to zero (%s)" % state)
        cannon_allow = redthis.get('permission_to_fire')
        lights_on = redthis.get('lights/monolith/state')
        GPIO.output(22,False)
        if (lights_on != "On"):
	    os.system("/usr/local/bin/switch_lights.sh on &")
        TIMESTAMP=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
	os.system("/usr/bin/raspivid -o /home/pi/CATCAM_DIR/catcam%s.h264 -t 12000 &" % TIMESTAMP)
        if (cannon_allow == "True"):
            logging.info("We have permission to fire")
            GPIO.output(27,False)
            sleep(1)
            GPIO.output(27,True) # Stop water pistol after 1 second
        sleep(10)
        GPIO.output(22,True) # Switch off lights after 10 seconds
        sleep(20)
        last_state = state
        if (lights_on != "On"):
	    os.system("/usr/local/bin/switch_lights.sh off &")
    else:
        last_state = state
    return last_state


while True:
    try:
        state = GPIO.input(25)
#        print ("State = %i" % state)
        last_state = detect_cat(state,last_state)
        sleep (0.1)
    except KeyboardInterrupt:
        GPIO.output(22,True)
        GPIO.output(27,True)
        GPIO.cleanup()
#    except:
#        print ("Bad stuff happened")
