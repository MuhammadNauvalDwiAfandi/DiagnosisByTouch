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
    if st == 'f' or st == 'F':
        print(f"Your current temperature is {tmp[1]}F")
    else:
        print(f"Your current temperatur is {tmp[0]}C")
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

time.sleep(1)

st = input('Satuan? C atau F: ')

logic(temp_chk())