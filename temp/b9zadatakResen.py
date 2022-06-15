#Zadatak B9 resen
import time
from signal import pause
from time import sleep
# from RPLCD.gpio import CharLCD
from RPLCD.i2c import CharLCD
from RPi import GPIO
from gpiozero import Button

#Prvobitna inicijalizacija vremena
startTime = time.time()

#Varijabla koja odredjuje da li je startovan
isTimerStarted = False

# i naravno varijabla koja registruje broj prekoracenja
prekoracenjeTimera = 0

#da stavimo koje vreme je vreme prekoracenja(max 10 minuta => 600 sekundi)
# pa je maksimalna vrednost 600
maksimalnoVreme = 10

btnPrvi = Button(21)
btnDrugi = Button(26)

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)

def pritisnutPrviTaster():
    """Callback funkcija koja registruje prvi taster pritisnut
     ovo je START/STOP taster.Kako je ovo callback funkcija ovde necemo
     meriti protok vremena vec samo kada se pritiska ovaj taster
    """
    # lcd.clear()
    # lcd.write_string('Pritisnut je taster 1')
    # print('pritisnut taster 1')
    global startTime
    global isTimerStarted
    # global vremePrekoracenja
    #Ovde proverava da li je pritisnut, ako nije izvrsava prvi blok
    if (not(isTimerStarted)):
        #Ovde ga startuje
        isTimerStarted = True
        startTime = time.time()
        #i naravno vreme vezano za prekoracenje
        # vremePrekoracenja = time.time()
    else:
        #Ovo se izvrsava deo ako je taster pritisnut
        # pa ovaj deo je nadlezan za RESET deo koda
        isTimerStarted = False

def pritisnutDrugiTaster():
    """Callback funkcija koja registruje drugi taster pritisnut
     ovo je RESET taster """
    # lcd.clear()
    # lcd.write_string('Pritisnut je taster 2')
    # print('pritisnut taster 2')
    # Proverava da li je tajmer startovan
    global startTime
    global isTimerStarted
    global prekoracenjeTimera
    # global vremePrekoracenja
    if(isTimerStarted):
        isTimerStarted = True
        startTime = time.time()
        # da resetujemo i prekoracenje timera
        prekoracenjeTimera = 0
        # zapravo moguce je da endtime nam uopste ne treba
        # vremePrekoracenja = time.time()
    # else:
        #Ako nije tajmer startovan 
        # nista ne radi

def updateDisplay():
    """Jednostavna funkcija koja updejtuje sta pise na displeju"""
    global startTime
    global prekoracenjeTimera
    # global vremePrekoracenja
    lcd.clear()
    #u prvom redu ispisujemo proteklo vreme...mozda treba da se enkoduje string
    elapsedTime = time.time() - startTime
    # posto resetuje tajmer vreme prekoracenja nam zapravo ne treba
    # vremePrekoracenja = elapsedTime

    lcd.write_string(time.strftime("%H:%M:%S",time.gmtime(elapsedTime)))
    lcd.cursor_pos = (1,0)
    #ovde takodje vidimo da li je prekoracen tajmer
    if(elapsedTime > maksimalnoVreme):
        prekoracenjeTimera = prekoracenjeTimera + 1
        # lcd.write_string(str('Prekoraceno je'.join(str(prekoracenjeTimera)).encode('utf8')))
        lcd.write_string('Prekoraceno je' + str(prekoracenjeTimera))
        # Posto je vreme u ovom slucaju prekoraceno onda se resetuje
        startTime = time.time()
    else:
        if(prekoracenjeTimera == 0):
            # sa ovim samo prvi put imamo poruku da nije prekoraceno
            lcd.write_string('Nije prekoraceno')
        else:
            lcd.write_string('Prekoraceno je ' + str(prekoracenjeTimera))

btnPrvi.when_pressed = pritisnutPrviTaster
btnDrugi.when_pressed = pritisnutDrugiTaster

lcd.write_string('Pozdrav')
print('program je startovan...')

#Ovde pocinjemo program
while True:
    if(isTimerStarted):
        #Ako je startovan merimo vreme
        updateDisplay()
        sleep(1)

pause()
