#Ovo je test zadatak b12
from signal import pause
from time import sleep
# from RPLCD.gpio import CharLCD
from RPLCD.i2c import CharLCD
from RPi import GPIO
from gpiozero import Button

btnPrvi = Button(21)

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)

def pritisnutPrviTaster():
    "Callback funkcija koja registruje prvi taster pritisnut"
    lcd.clear()
    lcd.write_string('Zdravo...')
    print('pritisnut taster 1')

btnPrvi.when_pressed = pritisnutPrviTaster

#Ovde pocinje izvrsenje programa
lcd.clear()
lcd.write_string('Dobar dan...')
print('program je startovan...')

pause()
