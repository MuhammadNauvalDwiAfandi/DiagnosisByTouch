import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def LEDGreen_On():
    GPIO.setup(25,GPIO.OUT)
    # set GPIO-a pin to HIGH
    GPIO.output(25,GPIO.HIGH)
    # pause for one second
    time.sleep(0.5)

def LEDGreen_Off():
    GPIO.setup(25,GPIO.OUT)
    # set GPIO-a pin to LOW
    GPIO.output(25,GPIO.LOW)
    # pause for one second
    time.sleep(0.5)

def LEDRed_On():
    GPIO.setup(8,GPIO.OUT)
    # set GPIO-a pin to LOW
    GPIO.output(8,GPIO.HIGH)
    # pause for one second
    time.sleep(0.5)

def LEDRed_Off():
    GPIO.setup(8,GPIO.OUT)
    # set GPIO-a pin to LOW
    GPIO.output(8,GPIO.LOW)
    # pause for one second
    time.sleep(0.5)

'''
Note: 
GPIO.setup(a,GPIO.OUT)
GPIO.output(a,GPIO.LOW)
GPIO.output(a,GPIO.HIGH)
 a is the number of gpio, a = 8 means gpio8
'''