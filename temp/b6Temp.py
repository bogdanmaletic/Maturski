# Zadatak B6 resen (Ovo je temp fajl u odnosu da pravi,koji je obrisan za potrebe snimanja)
#Taster1: 14, Taster2: 18, dioda1: 23,dioda2:25, dioda3: 7, dioda4: 21

from gpiozero import LEDBoard,Button
from time import sleep
from signal import pause

ledBrightCounter = 0

ledBoard = LEDBoard(23,25,7, pwm="True ")
btnUvecaj = Button(14)
btnSmanji = Button(18)

# Ovo je bilo za test program
# def upaliDiode():
#     """Callback f-ja kojom palimo diode"""
#     ledBoard.on()

# def ugasiDiode():
#     """Callback f-ja kojom gasimo diode"""
#     ledBoard.off()

# btnUvecaj.when_pressed = upaliDiode
# btnSmanji.when_pressed = ugasiDiode

def povecajLedBright():
    """Callback f-ja koja povecava sjaj dioda za 10 posto"""
    global ledBrightCounter
    if((ledBrightCounter >= 0) and (ledBrightCounter < 1)):
        #moramo da zaoukruzimo vrednosti sa tacnoscu na prvoj decimali
        ledBrightCounter = round(ledBrightCounter + 0.1, 1)
        print("Osvetljaj je sada ", ledBrightCounter)
        ledBoard.value = (ledBrightCounter,ledBrightCounter,ledBrightCounter)
    else:
        ledBrightCounter = 0
        print("Osvetljaj je sada ", ledBrightCounter)
        ledBoard.value = (ledBrightCounter,ledBrightCounter,ledBrightCounter)

def smanjiLedBright():
    """Callback f-ja koja smanjuje sjaj dioda za 10 posto"""
    global ledBrightCounter
    if((ledBrightCounter > 0) and (ledBrightCounter <= 1)):
        #moramo da zaoukruzimo vrednosti sa tacnoscu na prvoj decimali
        ledBrightCounter = round(ledBrightCounter - 0.1,1)
        print("Osvetljaj je sada ", ledBrightCounter)
        ledBoard.value = (ledBrightCounter,ledBrightCounter,ledBrightCounter)
    else:
        ledBrightCounter = 1
        print("Osvetljaj je sada ", ledBrightCounter)
        ledBoard.value = (ledBrightCounter,ledBrightCounter,ledBrightCounter)

btnUvecaj.when_pressed = povecajLedBright
btnSmanji.when_pressed = smanjiLedBright


print("Program je aktivan...")

ledBoard.value = (ledBrightCounter, ledBrightCounter, ledBrightCounter)

pause()
