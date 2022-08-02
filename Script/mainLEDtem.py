from temperature import *
from LED import *
import time

def temp_chk():
    print(' rom: '+ read_rom())
    print('Mengukur suhu, tunggu 2 menit')
    time.sleep(60)
    print('Tunggu 1 menit lagi...')
    time.sleep(30)
    print('Tunggu 30 detik lagi...')
    tmp = read_temp()
    print(f"Your current temperature is {tmp[0]}C {tmp[1]}F")
    return tmp[0]
    
def logic(tmp):
    if tmp <= 36:
        print("Error: Suhu terlalu rendah")
    elif tmp > 36 and tmp <= 37.5:
        print("Normal")
        LEDGreen_On()
    elif tmp > 37.5 and tmp <= 38.5:
        print("Sakit ringan")
        LEDRed_On()
    else:
        print('Sakit parah')
        for k in range(1,11):
            LEDRed_On()
            time.sleep(1)
            LEDRed_Off()
            time.sleep(1)


time.sleep(1)

logic(temp_chk())

time.sleep(5)

LEDRed_Off()
LEDGreen_Off()