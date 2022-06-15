# Test zadatak B16

from time import sleep
from signal import pause
from gpiozero import Button,LED

btnPrvi = Button(12)
btnDrugi = Button(16)

zelenaDioda = LED(20)
crvenaDioda = LED(21)

def pritisnutPrviTaster():
    """Jednostavna callback f-ja koja se izvrsava prilikom pritiska na 
    taster 1"""
    zelenaDioda.on()
    print('0')

def pritisnutDrugiTaster():
    """Jednostavna callback f-ja koja se izvrsava prilikom 
    pritiska na taster 2"""
    crvenaDioda.on()
    print('8')

btnPrvi.when_pressed = pritisnutPrviTaster
btnDrugi.when_pressed = pritisnutDrugiTaster
