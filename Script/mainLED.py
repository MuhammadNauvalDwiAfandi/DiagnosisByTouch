from LED import *
import time

while True:
    lampu = input('Green or Red: ')
    
    if lampu == 'Green':
        print('Selected: Green')
        kondisi = input('On or Off: ')

        if kondisi == 'On' or kondisi == 'on':
            LEDGreen_On()
            print('LED is on!')
            time.sleep(1)
        
        elif kondisi == 'Off' or kondisi == 'off':
            LEDGreen_Off()
            print('LED is off!')
            time.sleep(1)

        else:
            print('Invalid command!')

    elif lampu == 'Red':
        kondisi = input('On or Off: ')
        print('Selected: Red')

        if kondisi == 'On' or kondisi == 'on':
            LEDRed_On()
            print('LED is on!')
            time.sleep(1)
        
        elif kondisi == 'Off' or kondisi == 'off':
            LEDRed_Off()
            print('LED is off!')
            time.sleep(1)

        else:
            print('Invalid command!')

    elif lampu == 'secret':
        for k in range(1,11):
            LEDGreen_On()
            LEDRed_On()
            print('LED is on!')
            time.sleep(1)
            LEDGreen_Off()
            LEDRed_Off()
            print('LED is off!')
            time.sleep(1)

    else:
        print('Invalid command!')