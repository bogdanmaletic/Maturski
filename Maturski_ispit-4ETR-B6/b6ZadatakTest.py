# Zadatak B6 Test program
#Taster1: 14, Taster2: 18, dioda1: 23,dioda2:25, dioda3: 7, dioda4: 21

from gpiozero import LEDBoard,Button
from time import sleep
from signal import pause

ledBoard = LEDBoard(23,25,7)
btnUvecaj = Button(14)
btnSmanji = Button(18)

def upaliDiode():
    """Callback f-ja kojom palimo diode"""
    ledBoard.on()

def ugasiDiode():
    """Callback f-ja kojom gasimo diode"""
    ledBoard.off()

btnUvecaj.when_pressed = upaliDiode
btnSmanji.when_pressed = ugasiDiode

print("Program je aktivan...")

pause()
