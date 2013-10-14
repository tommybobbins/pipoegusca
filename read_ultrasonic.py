#!/usr/bin/python
import pifacecommon
import pifacedigitalio
import time
import datetime
import os
from os import path, access, R_OK

f = open('/usr/local/catcam/catlog.txt','a')
TIME_TO_SLEEP_AFTER_FIRING=10
SQUIRT_TIME=3
OUTPUT_RANGE = LED_RANGE = INPUT_RANGE = 8
LED_RANGE=6
INPUT_RANGE=8
OUTPUT_RANGE = 8
SWITCH_RANGE = 4
RELAY_RANGE = 2
PATH='/tmp/it_is_dark.txt'

def woo_woo():
    for i in range(2,8):
        pifacedigital.output_pins[i].value=1
	detect_cat()
        time.sleep(0.05)
    for i in reversed(range(2,8)):
        pifacedigital.output_pins[i].value=0
	detect_cat()
        time.sleep(0.05)

def detect_cat():
    input_on_off=pifacedigital.input_pins[7].value
    if (input_on_off == 1):
        f.write ('Input %i is %i\n' % (7,input_on_off)) 
        take_picture_on_trigger(7) 
	

def take_picture_on_trigger(pin):
        TIMESTAMP=datetime.datetime.now().strftime("%Y%m%d%H%M")
	f.write(TIMESTAMP)
        # We need to check whether we have to switch on the lights
        #
        if path.isfile(PATH):
            os.system("/usr/local/bin/switch_on_lights.sh")
	os.system("/usr/bin/raspivid -n -o /usr/local/catcam/catcam%s.h264 -t 5000 &" % TIMESTAMP)
        pifacedigital.relays[0].turn_on()
	time.sleep(SQUIRT_TIME)
        pifacedigital.relays[0].turn_off()
        time.sleep(TIME_TO_SLEEP_AFTER_FIRING)
        if path.isfile(PATH):
            os.system("/usr/local/bin/switch_off_lights.sh")


pifacedigitalio.init()
global pifacedigital
pifacedigital = pifacedigitalio.PiFaceDigital()
while True:
    woo_woo()
