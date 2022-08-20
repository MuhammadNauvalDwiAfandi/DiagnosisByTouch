import time

from temperature import *
from LED import *
from Oksi import *
from sendUbidots import *

LEDBlue_On()

def logic(temp, spo2, bpm):
    if 35 <= temp <= 37.2:
        return 'Normal'

    elif 37.2 < temp <= 38:
        return 'Sakit ringan'

    elif temp > 38:
        return 'Sakit parah'

    else:
        ...

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

def main():
    dta = startSensor()
    status = logic(dta[0], dta[1], dta[2])

    print(f"Temperature     : {dta[0]}")
    print(f'BPM             : {dta[1]}')
    print(f'SPO2            : {dta[2]}')
    print(f'Health status   : {status}')

    sendData(dta[1], 'Nauval', dta[2], status, dta[0])
    
    if status == 'Normal':
        LEDGreen_On()
    elif status == 'Sakit ringan':
        LEDRed_On()
    elif status == 'Sakit parah':
        for k in range(1,11):
            LEDRed_On()
            LEDRed_Off()

if __name__ == '__main__':
    main()
    time.sleep(10)
    LEDBlue_Off()
    LEDGreen_Off()
    LEDRed_Off()
    