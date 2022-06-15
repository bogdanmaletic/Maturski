from gpiozero import LED
from gpiozero import Button
from time import sleep
from signal import pause

#led = LED(15)
zelenaLed = LED(15)
zutaLed = LED(23)
crvenaLed = LED(25)

btn = Button(7)

def semafor():
    """Pokrece rad semafora"""
    crvenaLed.on()
    sleep(8)
    zutaLed.on()
    sleep(2)
    crvenaLed.off()
    zutaLed.off()
    zelenaLed.on()
    sleep(3)
    zelenaLed.off()
    sleep(0.5)
    zelenaLed.on()
    sleep(0.5)
    zelenaLed.off()
    sleep(0.5)
    zelenaLed.on()
    sleep(0.5)
    zelenaLed.off()
    sleep(0.5)
    zelenaLed.on()
    sleep(0.5)
    zelenaLed.off()
    zutaLed.on()
    sleep(2)
    zutaLed.off()

btn_stanje = 0

def simpleAdd():
    """Jednostavna callback f-ja koja ce nam inkrementirati
    globalnu promenljivu btn_stanje da bi imali informaciju
    da li je do sada bio pritisnuto dugme
    """
    global btn_stanje
    btn_stanje = btn_stanje + 1
    print("Od SimpleADD :", btn_stanje)

    # Alternativni nacin kako smo mogli da uradimo...
    # odmah zavrsava program
    # if(btn_stanje > 1):
    #     zelenaLed.off()
    #     zutaLed.off()
    #     crvenaLed.off()
    #     print("Finished...")
    #     quit()

btn.when_pressed = simpleAdd

while True:
    if ((btn.is_pressed) or (btn_stanje != 0)):
        semafor()        
        print("zavrsio se jedan ciklus ", btn.is_pressed)
        if (btn_stanje > 1):
            break
                
        

print("bla...zavrsen je program")
pause()
