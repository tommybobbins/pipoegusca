pipoegusca
==========

PiPoEGUSCA -  RaspberryPi Power over Ethernet Garden Ultrasonic Squirter Camera Alarm 


Deploy the init script into /etc/init.d/ and deploy the python script into /usr/local/bin

    pi@raspberrypi:$ cd pipoegusca


For the PiFace version:

    pi@raspberrypi:$ sudo cp read_ultrasonic.py /usr/local/bin

For the standard relay board version using the raw GPIO Pi Pins

    pi@raspberrypi:$ sudo cp read_ultrasonic_gpio.py

    pi@raspberrypi:$ sudo cp read-ultra.sh /etc/init.d/


Set the permissions:

    pi@raspberrypi:$ sudo chmod a+x /usr/local/bin/read-ultrasonic.py

    pi@raspberrypi:$ sudo chmod a+x /etc/init.d/read-ultra.sh

    pi@raspberrypi:$ sudo insserv read-ultra.sh

Make h264 video storage location:

    pi@raspberrypi:$ sudo mkdir /usr/local/catcam

    pi@raspberrypi:$ sudo chown pi /usr/local/catcam


Make all files written into /usr/local/catcam be owned by group pi:

    pi@raspberrypi:$ sudo chmod g+s /usr/local/catcam

Start it up:

    pi@raspberrypi:$ sudo /etc/init.d/read-ultra.sh start
