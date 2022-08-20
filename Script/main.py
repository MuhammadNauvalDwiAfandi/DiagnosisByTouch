import time
from unicodedata import name

from temperature import *
from LED import *
from Oksi import *
from sendUbidots import *
from rpi_lcd import LCD

lcd = LCD()
LEDRed_Off()
LEDGreen_Off()
LEDBlue_On()

def logic(temp, spo2, bpm):
    if 35 <= temp <= 37.2:
        return 'Normal'

    elif 37.2 < temp <= 38:
        return 'Sakit ringan'

    elif temp > 38:
        return 'Sakit parah'

    else:
        return 'Sakit'

def startSensor():
    '''
    Starting sensor, measure temperature, BPM, and SPO2
    Return (temperature, bpm, spo2)
    '''
    print('Mengukur...')

    oks = averageOksi()
    time.sleep(5)

    temp = read_temp()

    return temp[0], oks[0], oks[1]

def showLCD(status=None, temp=None, bpm=None, spo2=None):
    '''
    Show LCD Data from sensor
    '''
    lcd.text(status, 1)
    lcd.text(f'{temp}C H{bpm} O{spo2}', 2)

def main(name):
    dta = startSensor()
    status = logic(dta[0], dta[1], dta[2])

    print(f"Temperature     : {dta[0]}")
    print(f'BPM             : {dta[1]}')
    print(f'SPO2            : {dta[2]}')
    print(f'Health status   : {status}')

    sendData(dta[1], name, dta[2], status, dta[0])
    showLCD(status, dta[0], dta[1], dta[2])
    
    if status == 'Normal':
        LEDGreen_On()
    elif status in ['Sakit ringan', 'Sakit']:
        LEDRed_On()
    elif status == 'Sakit parah':
        for k in range(1,11):
            LEDRed_On()
            LEDRed_Off()

if __name__ == '__main__':
    name = input('Enter name: ')
    main(name)
    time.sleep(10)
    
    LEDBlue_Off()
    LEDGreen_Off()
    LEDRed_Off()
    