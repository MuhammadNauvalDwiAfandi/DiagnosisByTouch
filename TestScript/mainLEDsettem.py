from LED import *
import time
    
def logic(tmp):
    print(f'Your current temperature is {tmp}C')
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

if __name__ == '__main__':
    while True:
        setTem = float(input('Masukkan temperature: '))
        logic(setTem)

        time.sleep(1)
        input('Press enter key to continue...')