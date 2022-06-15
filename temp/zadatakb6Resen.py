# Zadatak B6 resen
#Taster1: 14, Taster2: 18, dioda1: 23,dioda2:25, dioda3: 7, dioda4: 21

from gpiozero import LEDBoard,Button
from time import sleep
from signal import pause

ledBoard = LEDBoard(23,25,7, pwm=True)
btnUvecaj = Button(14)
btnSmanji = Button(18)

ledBrightCounter = 0

# Test program
# def upaliDiode():
#     """Callback f-ja kojom palimo diode"""
#     ledBoard.on()

# def ugasiDiode():
#     """Callback f-ja kojom gasimo diode"""
#     ledBoard.off()

# btnUvecaj.when_pressed = upaliDiode
# btnSmanji.when_pressed = ugasiDiode

def povecajLedBright():
    "Callback f-ja koja povecava osvetljaj dioda"
    global ledBrightCounter
    if((ledBrightCounter >= 0) and (ledBrightCounter < 1)):
        #moramo da zaoukruzimo vrednosti sa tacnoscu na prvoj decimali
        ledBrightCounter = round(ledBrightCounter + 0.1,1)
        print("Osvetljaj je ", ledBrightCounter)
        ledBoard.value = (ledBrightCounter, ledBrightCounter, ledBrightCounter)
    else:      
        ledBrightCounter = 0
        print("Osvetljaj je ", ledBrightCounter)  
        ledBoard.value = (ledBrightCounter, ledBrightCounter, ledBrightCounter)

def smanjLedBright():
    """Callback f-ja koja smanjuje osvetljaj dioda"""
    global ledBrightCounter
    if((ledBrightCounter > 0) and (ledBrightCounter <= 1)):
        #moramo da zaoukruzimo vrednosti sa tacnoscu na prvoj decimali
        ledBrightCounter = round(ledBrightCounter - 0.1,1)
        print("Osvetljaj je ", ledBrightCounter)
        ledBoard.value = (ledBrightCounter, ledBrightCounter, ledBrightCounter)
    else:
        ledBrightCounter = 1
        print("Osvetljaj je ", ledBrightCounter)
        ledBoard.value = (ledBrightCounter, ledBrightCounter, ledBrightCounter)

btnUvecaj.when_pressed = povecajLedBright
btnSmanji.when_pressed = smanjLedBright

print("Program je aktivan...")

ledBoard.value = (ledBrightCounter,ledBrightCounter,ledBrightCounter)

pause()
