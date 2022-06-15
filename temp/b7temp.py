#Ovo je program zadatka B7

from signal import pause
from time import sleep
from RPLCD.gpio import CharLCD
from RPi import GPIO
from gpiozero import Button

btnPrvi = Button(13)
btnDrugi = Button(26)
btnTreci = Button(16)
btnCetvrti = Button(21)

lcd = CharLCD(pin_rs=15, pin_e=16, pins_data=[21, 22, 23, 24],
              numbering_mode=GPIO.BOARD,
              cols=16, rows=2, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              compat_mode=True)

pritisnutaSekvenca = []
sifra = [1,2,3,4]


def pritisnutPrviTaster():
    "Callback funkcija koja registruje prvi taster pritisnut"
    lcd.clear()
    lcd.write_string('Pritisnut je \n taster 1')
    pritisnutaSekvenca.append(1)

def pritisnutDrugiTaster():
    "Callback funkcija koja registruje drugi taster pritisnut"
    lcd.clear()
    lcd.write_string('Pritisnut je \n taster 2')
    pritisnutaSekvenca.append(2)

def pritisnutTreciTaster():
    "Callback funkcija koja registruje treci taster pritisnut"
    lcd.clear()
    lcd.write_string('Pritisnut je \n taster 3')
    pritisnutaSekvenca.append(3)

def pritisnutCetvrtiTaster():
    "Callback funkcija koja registruje cetvrti taster pritisnut"
    lcd.clear()
    lcd.write_string('Pritisnut je \n taster 4')
    pritisnutaSekvenca.append(4)

btnPrvi.when_pressed = pritisnutPrviTaster
btnDrugi.when_pressed = pritisnutDrugiTaster
btnTreci.when_pressed = pritisnutTreciTaster
btnCetvrti.when_pressed = pritisnutCetvrtiTaster

lcd.write_string('Pozdrav')
lcd.clear()

while True:
    if((pritisnutaSekvenca.__len__()) == 4):
        #Testiramo da li su iste
        if(pritisnutaSekvenca == sifra):
            lcd.clear()
            lcd.write_string('OK')
            #Ovo je ukoliko ne zelimo da izadjemo iz programa
            pritisnutaSekvenca = []
        else:
            lcd.clear()
            lcd.write_string('STOP')
            #resetujemo sekvencu i krecemo iznova
            pritisnutaSekvenca = []


#Poruka da je zavrsen program
print("Done...")
GPIO.cleanup()
quit()
