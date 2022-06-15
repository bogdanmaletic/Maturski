# Ovo je ceo drugi zadatak bez potenciometra
#Taster1: 14, Taster2: 18, dioda1: 23,dioda2:25, dioda3: 7, dioda4: 21

from gpiozero import LED,Button,LEDBoard
from signal import pause
from time import sleep

#aj da formiramo ledove
leds = LEDBoard(23,25,7,21)
btnSmer = Button(14)
btnUvecaj = Button(18)

ukljucenBrojDioda = 1
pauzaPromeneDioda = 0.5
selektorPrveDiode = 0
selektorZadnjeDiode = selektorPrveDiode + ukljucenBrojDioda - 1
maksimalniBrojDioda = 4

#Ovo je varijabla definisana za jednostavan nacin
#moze biti izmedju 1 i 4 i na osnovu njega bira nacin rada
selektorModa = 1

#Takodje ce biti definisan selektor smera
#moze da se bira izmedju 0 i 1(0 je smer sa leva na desno, dok 1 je obrnuti smer)
selektorSmera = 0


def ukljuciDiodeTest():
    """Ukljucuje diode i posle dve sekunde ih gasi"""
    print("Ukljucio si diode, pritisnuo si SMER")
    leds.on()
    #sleep(2)
    # leds.off()

def iskljuciDiodeTest():
    """Iksljucije diode"""
    print("Iskljucio si diode, pritisnuo si UVECAJ")
    leds.off()
    print("Done...")
    quit()


def uvecaj():
    """Povecava broj dioda za jedan"""
    #Prvo treba da resetuje da ne bi upadali u probleme
    global selektorPrveDiode
    global ukljucenBrojDioda
    global maksimalniBrojDioda
    global selektorZadnjeDiode
    print("Pritisnuo si dugme uvecaj")
    leds.off()
    selektorPrveDiode = 0
    if(ukljucenBrojDioda < (maksimalniBrojDioda - 1)):
        ukljucenBrojDioda = ukljucenBrojDioda + 1
    else:
        ukljucenBrojDioda = 1
    selektorZadnjeDiode = selektorPrveDiode + ukljucenBrojDioda - 1
    selektorPrveDiode = 0

def seljacki():
    """Prosto inkrementator koji smo razvijali
    pod slucajem da ne radi osnovni, deo
    """
    global ukljucenBrojDioda
    if (ukljucenBrojDioda < maksimalniBrojDioda):
        ukljucenBrojDioda = ukljucenBrojDioda + 1
    else:
        ukljucenBrojDioda = 1

# Ova dva definise vezano za test
# btnSmer.when_pressed = ukljuciDiodeTest
# btnUvecaj.when_pressed = iskljuciDiodeTest


#Ovo je odgovor na dogadjaj kada se dugme pritisne u komplikovanom slucaju
# btnUvecaj.when_pressed = uvecaj
#btnSmer.when_pressed = iskljuciDiodeTest
#Ovde krece program

def jednostavanUvecaj():
    """Jednostavna callback funkcija koja samo menja selektor moda, menja 
    selektor ali tako da ostane u granicama od 1 do 4"""
    global selektorModa
    if(selektorModa < 4):
        selektorModa = selektorModa + 1
    else:
        selektorModa = 1

def jednostavnoSmer():
    """Jednostavna callback f-ja koja menja selektor smera, menja selektor smera 
    ali tako da moze da bude jedan ili nula"""
    global selektorSmera
    if(selektorSmera == 0):
        selektorSmera = 1
    else:
        selektorSmera = 0

#jednostavna varijanta
btnUvecaj.when_pressed = jednostavanUvecaj
btnSmer.when_pressed = jednostavnoSmer

print("Program je aktivan")

while True:
    #Dakle koristimo leds.on(1,2) na primer
    #prvi je selektor koja je prva, posle ide vrednost do koje je ukljucena vrednost
    # bice zamenjena varijablom
    #umesto klasicnog poziva leds.on(1,2) moramo na drugi nacin
    # leds.on(selektorPrveDiode,selektorZadnjeDiode)
    #moramo preko for-a

    #Aj seljacki
    # ipak necemo seljacki lepo radi i ovako....
    # if (ukljucenBrojDioda == 1):
    #     for led in leds[selektorPrveDiode:(selektorZadnjeDiode + ukljucenBrojDioda)]:
    #         led.on()
    #     sleep(pauzaPromeneDioda)
    #     if(selektorPrveDiode < maksimalniBrojDioda):
    #         selektorPrveDiode = selektorPrveDiode + 1
    #         selektorZadnjeDiode = selektorZadnjeDiode



    #Komplikovan nacin(koji radi)

    # for led in leds[selektorPrveDiode:(selektorZadnjeDiode + 1)]:
    #     led.on()
    # sleep(pauzaPromeneDioda)
    # leds.off()
    # if(selektorPrveDiode < (maksimalniBrojDioda - ukljucenBrojDioda)):
    #     selektorPrveDiode = selektorPrveDiode + 1
    #     selektorZadnjeDiode = selektorZadnjeDiode + 1
    #     leds.off()
    # else:
    #     selektorPrveDiode = 0
    #     #na ovakav nacin definisemo indeks zadnje diode koja treba da bude ukljucena
    #     selektorZadnjeDiode = selektorPrveDiode + ukljucenBrojDioda -1
    #     leds.off()

    #Kraj Komplikovanog nacina

    
    #Jednostavan nacin(Koristi selektor moda) i selektor smera
    if ((selektorModa == 1) and (selektorSmera == 0)):
        #dakle biramo koje su diode ukljucene, pa onda nakon spavanja menjamo stanja
        #naravno prvo ih pogasimo da ne ostane neka upaljena
        leds.off()
        leds.value = (1,0,0,0)
        sleep(pauzaPromeneDioda)
        leds.value = (0,1,0,0)
        sleep(pauzaPromeneDioda)
        leds.value = (0,0,1,0)
        sleep(pauzaPromeneDioda)
        leds.value = (0,0,0, 1)
        sleep(pauzaPromeneDioda)
        #Sa ovim je jedan ciklus promenjen, gasimo diode da ne ostane ukljucena
        leds.off()
    if((selektorModa == 2) and (selektorSmera == 0)):
        #Ovo je drugi mod, pale se dve diode
        #ali da proverimo da su sve ugasene
        leds.off()
        leds.value = (1,1,0,0)
        sleep(pauzaPromeneDioda)
        leds.value = (0,1,1,0)
        sleep(pauzaPromeneDioda)
        leds.value = (0,0,1,1)
        sleep(pauzaPromeneDioda)
        #i da ne zaboravimo da pogasimo diode
        leds.off()
    if((selektorModa == 3) and (selektorSmera == 0)):
        #ovo je treci mod kada su sve upaljene
        #da se uverimo da su sve ugasene
        leds.off()
        leds.value = (1,1,1,0)
        sleep(pauzaPromeneDioda)
        leds.value = (0,1,1,1)
        sleep(pauzaPromeneDioda)
        leds.value = (1,0,1,1)
        sleep(pauzaPromeneDioda)
        leds.value = (1,1,0,1)
        sleep(pauzaPromeneDioda)
        leds.value = (1,1,1,0)
        sleep(pauzaPromeneDioda)
        #i da ne zaboravimo da pogasimo diode
        leds.off()
    if((selektorModa == 4) and (selektorSmera == 0)):
        #Ovo je cetvrti mod kada su diode sve upaljene
        leds.on()
    #sada uvodimo i selektor smera
    if((selektorModa == 1) and (selektorSmera == 1)):
        #Ovo je prvi mod sa jednom diodom i obrnutim smerom
        #prvo da se uverimo da li su sve diode iskljucene
        leds.off()
        leds.value = (0,0,0,1)
        sleep(pauzaPromeneDioda)
        leds.value = (0,0,1,0)
        sleep(pauzaPromeneDioda)
        leds.value = (0,1,0,0)
        sleep(pauzaPromeneDioda)
        leds.value = (1,0,0,0)
        sleep(pauzaPromeneDioda)
        #sa ovim je ciklus promenjen pa mozemo da pogasimo diode
        # i da pocnemo iz pocetka
        leds.off()
    if((selektorModa == 2) and (selektorSmera == 1)):
        #Ovo je drugi mod sa dve diode i obrnutim smerom
        #da se uverimo da su sve diode iskljucene
        leds.off()
        leds.value = (0,0,1,1)
        sleep(pauzaPromeneDioda)
        leds.value = (0,1,1,0)
        sleep(pauzaPromeneDioda)
        leds.value = (1,1,0,0)
        sleep(pauzaPromeneDioda)
        #ciklus je zavrsen i da se uverimo da su sve diode iskljucene
        leds.off()
    if((selektorModa == 3) and (selektorSmera == 1)):
        #ovo je treci mod sa ukljucene tri diode i obrnutim smerom
        #da se uverimo da su sve diode iskljucene
        leds.off()
        leds.value = (0,1,1,1)
        sleep(pauzaPromeneDioda)
        leds.value = (1,1,1,0)
        sleep(pauzaPromeneDioda)
        leds.value = (1,1,0,1)
        sleep(pauzaPromeneDioda)
        leds.value = (1,0,1,1)
        sleep(pauzaPromeneDioda)
        leds.value = (0,1,1,1)
        #ciklus je zavrsen i da se uverimo da su sve diode iskljucene
        leds.off()
    if((selektorModa == 4) and (selektorSmera == 1)):
        #ovo je cetvrti mod kada su sve diode upaljene
        leds.on()







leds.off()
pause()
