from LED import *
import time

a = 25 #Number of gpio, a = 25 means gpio25

while True:
    kondisi = input('On or Off: ')
    if kondisi == 'On' or kondisi == 'on':
        LED_On(a)
        print('LED is on!')
        time.sleep(1)
    
    elif kondisi == 'Off' or kondisi == 'off':
        LED_Off(a)
        print('LED is off!')
        time.sleep(1)

    elif kondisi == 'secret':
        for k in range(1,11):
            LED_On(a)
            print('LED is on!')
            time.sleep(1)
            LED_Off(a)
            print('LED is off!')
            time.sleep(1)

    else:
        print('Invalid command!')