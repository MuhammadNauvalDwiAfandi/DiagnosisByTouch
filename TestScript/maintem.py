from temperature import *
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
    elif tmp > 37.5 and tmp <= 38.5:
        print("Sakit ringan")
    else:
        print('Sakit parah')

if __name__ == '__main__':
    while True:
        logic(temp_chk())
        time.sleep(1)

        input('Press enter key to continue...')