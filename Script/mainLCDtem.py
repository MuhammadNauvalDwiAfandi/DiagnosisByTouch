from rpi_lcd import LCD
from mainLEDtem import temp_chk
import time

lcd = LCD()

while True:
    lcd.text(f'T = {temp_chk()}',1)
    time.sleep(1)
    input('Press enter to continue...')