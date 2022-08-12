## DIAGNOSIS BY TOUCH
This project is made for Samsung Innovation Campus Batch 3 Stage 3. This repository was made to track the progress we make to build an IoT device.

You can see the full design here:
[Product Design](https://docs.google.com/presentation/d/1qDALvNa_1nn2KUcgnvzO5qR8LjPEqhXRsp-H-NQz1CA/edit?usp=sharing)

We are using:

 - DS18B20 Body Temperature Sensor
 - Max30102 Pulse Oximeter and Hearth Rate Sensor
 - Raspberry Pi 3 Model B Rev 1.2
 - LED light
 - LCD I2C


## Script Content

All scripts can be found at *Script* folder

|File Name|Content  |
|--|--|
| temperature.py |All the functions necessary to read DS18B20 temperature sensor  |
|maintem.py|Function to read and some logic to determine health based on body temperature|
|LED.py|All functions for controlling LED light |
|mainLED.py|Script to control LED light. Required LED.py|
|mainLEDtem.py| Get temperature data using DS18B20 sensor, then using logic to control LED light with given data|
|mainLEDsettem.py| Similar with mainLEDtem.py, instead of using data from actual sensor, user can input their own data to control LED light (for testing purpose)|


**Logic LED and Temperature**

mainLEDtem.py and mainLEDsettem.py logic:
 - Less than or equal to 36C, show `Error: Suhu terlalu rendah`
 - Between 36C and 37,5C, show `Normal` and turn on LED Green
 - Between 37,5C and 38,5C, show `Sakit ringan` and turn on LED Red
 - Above 38,5C, show `Sakit parah` and make LED Red blink


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


## LED
**Wiring to Raspberry Pi**

LED Green Wiring
|LED Green|Raspberry Pi  |
|--|--|
|Anode (longer leg)|Raspberry Pi GPIO25|
|Cathode (shorter leg) |Resistor 220 ohm|
|Resistor 220 ohm | Raspberry Pi GND|

LED Red Wiring
| LED Red | Raspberry Pi |
|--|--|
|Anode (longer leg)|Raspberry Pi GPIO8|
|Cathode (shorter leg) |Resistor 220 ohm|
|Resistor 220 ohm | Raspberry Pi GND|


See wiring diagram at Design folder or at Documentation for RL application

**Script**

Here we are using Python to change the LED state. In the *script* folder, for LED there are two Python scripts, one (LED.py) contains all necessary functions for controlling the LED, another one (mainLED.py) contains script to control the LED light.

**How to Use**

 - Copy the script (mainLED.py and LED.py) to Raspberry Pi. *All the scripts must be put in one folder!*
 - In Raspberry Pi, using terminal, run mainLED.py `python mainLED.py`
 - Enter either `Green` or `Red`
 - Then enter either `On` or `Off` to control the LED


## LCD I2C
**Wiring to Raspberry Pi**

| LCD I2C |Raspberry Pi  |
|--|--|
| GND | Raspberry Pi GND|
| VCC | Raspberry Pi 5V|
| SDA | Raspberry Pi GPIO2|
| SCL | Raspberry Pi GPIO3|


See wiring diagram at Design folder or at Documentation for RL application

**Enable I2C**

 - Open terminal, type `sudo raspi-config`
 - Select *Interfacing Option*
 - Enable *I2C*
 - Back to terminal, then reboot system `sudo reboot`
 - Open terminal again, type `i2cdetect -y 1`. The *i2cdetect* command can be used to see what is connected and what the addresses are. Most common are `27 hexadecimal`.

**Install Python Library**

 - Using terminal. type `sudo pip3 install rpi_lcd`
 - This library has the default 27 address hard-coded. If your display has a different address, you will need to change it. Find the library using `sudo find /usr/local –name rpi_lcd 2> /dev/null`
 - Find *rpi_lcd*, commonly it can be found at `/usr/local/lib/(python version)/dist-packages/rpi_lcd`
 - Get into that directory using `cd /usr/local/lib/(python version)/dist-packages/rpi_lcd`
 - Type `nano __init__.py`, locate `LCD class`, `def __init__(self, address = 27, ...)`
 - Change `address = 27` to your address that show at `i2cdetect` command

**Script**

Here we are using Python to control the LCD. In the *script* folder, there is testLCD.py. It contains a function and some information about how to control the LCD.

**How to Use**

Using terminal, run the script `sudo python testLCD.py`

