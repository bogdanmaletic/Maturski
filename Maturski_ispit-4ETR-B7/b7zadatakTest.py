#Ovo je test program zadatka B7

from signal import pause
from time import sleep
# from RPLCD.gpio import CharLCD
from RPLCD.i2c import CharLCD
from RPi import GPIO
from gpiozero import Button

btnPrvi = Button(13)
btnDrugi = Button(26)
btnTreci = Button(16)
btnCetvrti = Button(21)

#Ovo je za GPIO varijantu povezivanja
# lcd = CharLCD(pin_rs=15, pin_e=16, pins_data=[21, 22, 23, 24],
#               numbering_mode=GPIO.BOARD,
#               cols=16, rows=2, dotsize=8,
#               charmap='A02',
#               auto_linebreaks=True,
#               compat_mode=True)

#Ovo je za i2c varijantu povezivanja
#Ne zaboraviti da se pre pustanja u rad proveri adresa preko i2cdetect
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

def pritisnutTreciTaster():
    "Callback funkcija koja registruje treci taster pritisnut"
    lcd.clear()
    lcd.write_string('Pritisnut je taster 3')
    print('pritisnut taster 3')

def pritisnutCetvrtiTaster():
    "Callback funkcija koja registruje cetvrti taster pritisnut"
    lcd.clear()
    lcd.write_string('Pritisnut je taster 4')
    print('pritisnut taster 4')

btnPrvi.when_pressed = pritisnutPrviTaster
btnDrugi.when_pressed = pritisnutDrugiTaster
btnTreci.when_pressed = pritisnutTreciTaster
btnCetvrti.when_pressed = pritisnutCetvrtiTaster

#Ovo moramo da stavimo u ovom slucaju
# lcd.clear()
lcd.write_string('Pozdrav')
print('program je startovan...')

# print('Ovim zavrsavamo program i cistimo lcd displej')
# lcd.clear()
# lcd.close(clear=True)

pause()


#Naglasiti u videu
#Poruka da je zavrsen program,ali u slucaju bez pause
# Test program mora da nastavi da radi pa se mora staviti pauza
# print("Done...")
# GPIO.cleanup()
# quit()
