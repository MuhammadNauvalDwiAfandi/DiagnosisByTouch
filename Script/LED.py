import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(a,GPIO.OUT)

def LED_On(a):
    # set GPIO-a pin to HIGH
    GPIO.output(a,GPIO.HIGH)
    # pause for one second
    time.sleep(1)

def LED_Off(a):
    # set GPIO-a pin to LOW
    GPIO.output(a,GPIO.LOW)
    # pause for one second
    time.sleep(1)

#Note: a is the number of gpio, a = 8 means gpio8