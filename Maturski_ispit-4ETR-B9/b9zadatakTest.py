#Ovo je test zadatka B9

from signal import pause
from time import sleep
# from RPLCD.gpio import CharLCD
from RPLCD.i2c import CharLCD
from RPi import GPIO
from gpiozero import Button

btnPrvi = Button(21)
btnDrugi = Button(26)

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)

def pritisnutPrviTaster():
    "Callback funkcija koja registruje prvi taster pritisnut"
    lcd.clear()
    lcd.write_string('Pritisnut je taster 1')
    print('pritisnut taster 1')


def pritisnutDrugiTaster():
    "Callback funkcija koja registruje drugi taster pritisnut"
    lcd.clear()
    lcd.write_string('Pritisnut je taster 2')
    print('pritisnut taster 2')

btnPrvi.when_pressed = pritisnutPrviTaster
btnDrugi.when_pressed = pritisnutDrugiTaster

lcd.write_string('Pozdrav')
print('program je startovan...')

pause()
