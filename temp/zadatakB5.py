# B5 zadatak 

from time import sleep
from RPLCD.i2c import CharLCD
import Adafruit_DHT
from RPi import GPIO
from gpiozero import LED
from math import floor

print("Program je pokrenut...")

grejac = LED(21)
ventilator = LED(20)

# Definisemo prag temperature
pragTemperature = 25

# Jednostavna funkcija za paljenje grejaca i gasenje ventilatora
def upaliGrejac():
    grejac.on()
    ventilator.off()

# Jednostavna funkcija za paljenje ventilatora i gasenje grejaca
def upaliVentilator():
    ventilator.on()
    grejac.off()

# Jednostavna funkcija koja gasi ventilator i grejac
def ugasiGrejacIVentilator():
    ventilator.off()
    grejac.off()

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)

# lcd.clear()
#Ovo je za jedno merenje
# humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,18)
# if humidity is not None and temperature is not None:
#     print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
#     lcd.clear()
#     # lcd.write_string('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
#     lcd.write_string('Temp {0:0.1f}C  {0:0.1f} C'.format(temperature,pragTemperature))
#     lcd.cursor_pos(1,0)
#     lcd.write_string('Vlaga {0:0.1f} %'.format(humidity))
#     grejac.on()
#     ventilator.on()

#     #Da pogasimo sve
#     print("Gasi se sve za deset sekundi ne iskljucivati program")
#     sleep(10)
#     lcd.clear()
#     grejac.off()
#     ventilator.off()


# else:
#     print('Failed to get reading. Try again!')


while True:
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,15)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        lcd.clear()
        # lcd.write_string('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        lcd.write_string('Temp {0:d}C    {1:d} C'.format(int(temperature),int(pragTemperature)))
        lcd.cursor_pos = (1,0)
        lcd.write_string('Vlaga {0:0.1f} %'.format(humidity))

        if(temperature < pragTemperature):
            upaliGrejac()
        if(temperature > pragTemperature):
            upaliVentilator()
        if(temperature ==  floor(pragTemperature)):
            ugasiGrejacIVentilator()
        
        sleep(2)

        #Ovo dodajemo pa cemo da uklonima
        # ugasiGrejacIVentilator()
        # lcd.clear()

        #Da pogasimo sve
        # print("Gasi se sve za deset sekundi ne iskljucivati program")
        # sleep(10)
        # lcd.clear()
        # grejac.off()
        # ventilator.off()


    else:
        print('Failed to get reading. Try again!')

