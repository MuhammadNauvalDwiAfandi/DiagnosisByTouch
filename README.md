## DIAGNOSIS BY TOUCH
This project is made for Samsung Innovation Campus Batch 3 Stage 3. This repository was made to track the progress we make to build an IoT device.
We are using:

 - DS18B20 Body Temperature Sensor
 - Max30102 Pulse Oximeter and Hearth Rate Sensor
 - Raspberry Pi 3 Model B Rev 1.2
 - LED light
 - LCD I2C
## DS18B20 Setup
**Wiring to Raspberry Pi**
|DS18B20|Raspberry Pi  |
|--|--|
|GND (Black wire) |Raspberry Pi GND |
|DQ (Yellow wire)|Raspberry Pi GPIO17|
|VDD (Red wire)|Resistor 4,7k ohm|
|Resistor|Raspberry Pi 3v3|

See wiring diagram at Design folder or at Documentation for RL application

**Enable 1-Wire**
 - Open terminal, type `sudo raspi-config`
 - Select *Interfacing Option*
 - Enable *1-Wire*
 - Back to terminal, type `sudo modprobe w1_gpio` then `sudo modprobe w1_therm`
 - Edit config.txt file, type `sudo nano /boot/config.txt`
 - Append new line, and type `dtoverlay=w1-gpio-pullup,gpiopin=17`

**Read Temperature**

 - Change directory to /sys/bus/w1/devices, type `cd /sys/bus/w1/devices`
 - Check the directory using `ls` It should contain folder *28-xxxxxxxxxxxx*
 - Hop into that folder
 - Read the temperature using `cat w1-slave`
 - The YES in the first line indicates CRC check success (Data Valid). The number following t= is the temperature
 
**Script Read Temperature**
Here we are using Python to show the temperature. In the *Script* folder, for DS18B20 there are two Python scripts, one (temperature.py) contains all necessary functions to read temperature for the sensor, another one (maintem.py) contains function to read and some logic to determine health based on body temperature.

**How to Use**

 - Copy the script (maintem.py and temperature.py) to Raspberry Pi. *All the scripts must be put in one folder!*
 - Hold the sensor using one of your hands
 - In Raspberry Pi, run terminal, navigate to where you put the script
 - Run the script by typing `sudo python maintem.py` *Note: this script must be run by the root user*
 
 **Important Note**
For now, this is just proof of concept!


## LED Green
**Wiring to Raspberry Pi**
|LED Green|Raspberry Pi  |
|--|--|
|Anode (longer leg)|Raspberry Pi GPIO25|
|Cathode (shorter leg) |Resistor 220 ohm|
|Resistor 220 ohm | Raspberry Pi GND|


See wiring diagram at Design folder or at Documentation for RL application

**Script**
Here we are using Python to change the LED state. In the *script* folder, for LED there are two Python scripts, one (LED.py) contains all necessary functions for controlling the LED, another one (mainLED.py) contains script to control the LED light.

**How to Use**
 - Copy the script (mainLED.py and LED.py) to Raspberry Pi. *All the scripts must be put in one folder!*
 - In Raspberry Pi, using terminal, run mainLED.py `python mainLED.py`
 - Enter either `On` or `Off` to control the LED
