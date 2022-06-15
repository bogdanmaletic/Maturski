# b12 zadatak resen

from signal import pause
from time import sleep
# from RPLCD.gpio import CharLCD
from RPLCD.i2c import CharLCD
from RPi import GPIO
from gpiozero import Button
from random import randrange

btnPrvi = Button(21)

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)

redniBrojBacanja = 1
# dobijeniSlucajniBroj = 0
daLiJeProslaPorukaDobrodoslice = False

def pritisnutPrviTaster():
    """Callback funkcija koja registruje prvi taster pritisnut i za svaki pritisak
    generise slucajan broj i ispisuje poruku na ekranu lcd displeja"""
    global redniBrojBacanja
    global daLiJeProslaPorukaDobrodoslice
    lcd.clear()
    # lcd.write_string('usao je u callback')
    # print('hello iz cakkbacka')
    print('Da li je guard ukinut', daLiJeProslaPorukaDobrodoslice)
    if(daLiJeProslaPorukaDobrodoslice):
        lcd.clear()
        dobijeniSlucajniBroj = randrange(1,7,1)
        tempString = "Vas " + str(redniBrojBacanja) + " broj je " + str(dobijeniSlucajniBroj)
        lcd.write_string(tempString)
        if(dobijeniSlucajniBroj == 6):
            lcd.cursor_pos = (1,0)
            lcd.write_string('Ponovite bacanje')
        redniBrojBacanja = redniBrojBacanja + 1
        print('pritisnut taster 1')

def porukaDobrodoslice():
    """Jednostavna poruka dobrodoslice koja pomera poruku 3 sekunde i 3 sekunde vraca"""
    global daLiJeProslaPorukaDobrodoslice
    global lcd
    lcd.clear()
    lcd.write_string('Dobro dosli')
    # lcd.clear()
    sleep(1)
    lcd.clear()
    lcd.write_string(' Dobro dosli')
    # lcd.clear()
    sleep(1)
    lcd.clear()
    lcd.write_string('  Dobro dosli')
    # lcd.clear()
    sleep(1)
    lcd.clear()
    lcd.write_string('   Dobro dosli')
    # lcd.clear()
    sleep(1)
    lcd.clear()
    lcd.write_string('  Dobro dosli')
    # lcd.clear()
    sleep(1)
    lcd.clear()
    lcd.write_string(' Dobro dosli')
    # lcd.clear()
    sleep(1)
    lcd.clear()
    lcd.write_string('Dobro dosli')
    daLiJeProslaPorukaDobrodoslice = True
    

btnPrvi.when_pressed = pritisnutPrviTaster

#Ovde pocinje izvrsenje programa
print('program je startovan...')
# lcd.clear()
# lcd.write_string('Ok program je startovan')
# sleep(5)
porukaDobrodoslice()
# lcd.clear()
# lcd.write_string('zasto nece')
# sleep(5)
lcd.clear()
lcd.write_string('Baci kocku')


pause()
