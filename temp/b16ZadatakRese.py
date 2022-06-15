#Resen zadatak B16
from time import sleep
from signal import pause
from gpiozero import Button,LED

btnPrvi = Button(12)
btnDrugi = Button(16)

zelenaDioda = LED(20)
crvenaDioda = LED(21)

brojSlobodnihMesta = 5

daliJePritisnutTaster1 = False
daliJePritisnutTaster2 = False

def pritisnutPrviTaster():
    """Jednostavna callback f-ja koja se izvrsava prilikom pritiska na 
    taster 1"""
    # zelenaDioda.on()
    # print('0')
    global daliJePritisnutTaster1
    global daliJePritisnutTaster2

    zelenaDioda.on()
    sleep(0.5)
    zelenaDioda.off()
    
    daliJePritisnutTaster1 = True
    if(daliJePritisnutTaster2):
        #Ovaj se izvrsava kada je prethodno pritisnut Taster 2
        #U prevodu kada se izlazi sa parkinga
        brojSlobodnihMesta = brojSlobodnihMesta + 1
        print('Broj slobodnih mesta: ', brojSlobodnihMesta)
        daliJePritisnutTaster1 = False
        daliJePritisnutTaster2 = False


def pritisnutDrugiTaster():
    """Jednostavna callback f-ja koja se izvrsava prilikom 
    pritiska na taster 2"""
    # crvenaDioda.on()
    # print('8')
    global daliJePritisnutTaster1
    global daliJePritisnutTaster2

    crvenaDioda.on()
    sleep(0.5)
    crvenaDioda.off()
    
    daliJePritisnutTaster2 = True
    if(daliJePritisnutTaster1):
        #Ovaj blok se izvrsava kada je pretjodno pritisnut Taster 1
        #U prevodu kada se ulazi na parking
        brojSlobodnihMesta = brojSlobodnihMesta - 1
        print('Broj slobodnih mesta: ', brojSlobodnihMesta)
        daliJePritisnutTaster1 = False
        daliJePritisnutTaster2 = False

btnPrvi.when_pressed = pritisnutPrviTaster
btnDrugi.when_pressed = pritisnutDrugiTaster

# Taster1 mora da bude pritisnut => Taster2 mora da bude pritisnut => Vozilo je uslo i brojac slobodnih mesta se smanjuje za 1
