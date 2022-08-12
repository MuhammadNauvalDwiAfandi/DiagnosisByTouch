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
        time.sleep(5)
        LEDGreen_Off()

    elif tmp > 37.5 and tmp <= 38.5:
        print("Sakit ringan")
        LEDRed_On()
        time.sleep(5)
        LEDRed_Off()
        
    else:
        print('Sakit parah')
        for k in range(1,11):
            LEDRed_On()
            LEDRed_Off()

while True:
    logic(temp_chk)
    time.sleep(1)

    input('Press enter key to continue...')