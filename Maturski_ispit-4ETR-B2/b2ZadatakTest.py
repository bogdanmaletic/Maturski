# Ok ovo je pocetak prvog zadatka
#Taster1: 14, Taster2: 18, dioda1: 23,dioda2:25, dioda3: 7, dioda4: 21

from gpiozero import LED,Button,LEDBoard
from signal import pause
from time import sleep

#aj da formiramo ledove
leds = LEDBoard(23,25,7,21)
btnSmer = Button(14)
btnUvecaj = Button(18)



def ukljuciDiode():
    """Ukljucuje diode i posle dve sekunde ih gasi"""
    print("Ukljucio si diode, pritisnuo si SMER")
    leds.on()
    #sleep(2)
    # leds.off()

def iskljuciDiode():
    """Iksljucije diode"""
    print("Iskljucio si diode, pritisnuo si UVECAJ")
    leds.off()

btnSmer.when_pressed = ukljuciDiode
btnUvecaj.when_pressed = iskljuciDiode

print("Program je aktivan")
pause()
