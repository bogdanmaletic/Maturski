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

# Ovo je za GPIO nacin povezivanja
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

unetaSekvenca = []
sifra = [1,2,3,4]

def pritisnutPrviTaster():
    "Callback funkcija koja registruje prvi taster pritisnut"
    lcd.clear()
    lcd.write_string('Pritisnut je taster 1')
    unetaSekvenca.append(1)
    print('Sekvenca je:',unetaSekvenca)
    #Proveravamo da li je uneta dobra sifra
    proveraSifre()

def pritisnutDrugiTaster():
    "Callback funkcija koja registruje drugi taster pritisnut"
    lcd.clear()
    lcd.write_string('Pritisnut je taster 2')
    unetaSekvenca.append(2)
    print('Sekvenca je:',unetaSekvenca)
    #Proveravamo da li je uneta dobra sifra
    proveraSifre()

def pritisnutTreciTaster():
    "Callback funkcija koja registruje treci taster pritisnut"
    lcd.clear()
    lcd.write_string('Pritisnut je taster 3')
    unetaSekvenca.append(3)
    print('Sekvenca je:',unetaSekvenca)
    #Proveravamo da li je uneta dobra sifra
    proveraSifre()

def pritisnutCetvrtiTaster():
    "Callback funkcija koja registruje cetvrti taster pritisnut"
    lcd.clear()
    lcd.write_string('Pritisnut je taster 4')
    unetaSekvenca.append(4)
    print('Sekvenca je:',unetaSekvenca)
    #Proveravamo da li je uneta dobra sifra
    proveraSifre()

#Aj da probamo malo finije ovo da resimo umesto while True petlje
def proveraSifre():
    """Jednostavna funkcija koja proverava da li je uneta sekvenca jednaka sifri"""
    global unetaSekvenca
    global sifra
    if((len(unetaSekvenca)) == 4):
        if(unetaSekvenca == sifra):
            lcd.clear()
            lcd.write_string('OK')
            unetaSekvenca = []
        else:
            lcd.clear()
            lcd.write_string('STOP')
            unetaSekvenca = []

btnPrvi.when_pressed = pritisnutPrviTaster
btnDrugi.when_pressed = pritisnutDrugiTaster
btnTreci.when_pressed = pritisnutTreciTaster
btnCetvrti.when_pressed = pritisnutCetvrtiTaster

# Varijanta sa while True -- generalno problem je sa velikim zauzecem resursa posto
#  non stop vrti u petlji i proverava da li je duzina sekvence 4... umesto toga dodali 
#  smo varijantu da proverava samo kada je taster pritisnut
# while True:
#     if((len(unetaSekvenca)) == 4):
#         if(unetaSekvenca == sifra):
#             lcd.clear()
#             lcd.write_string('OK')
#             unetaSekvenca = []
#         else:
#             lcd.clear()
#             lcd.write_string('STOP')
#             unetaSekvenca = []

print('Program je pokrenut')
lcd.write_string('Pozdrav')
# lcd.clear()



#Poruka da je zavrsen program
pause()
print("Done...")
# GPIO.cleanup()
quit()
