# B5 zadatak test

from time import sleep
from RPLCD.i2c import CharLCD
import Adafruit_DHT
from RPi import GPIO
from gpiozero import LED

grejac = LED(21)
ventilator = LED(20)

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,18)
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    lcd.clear()
    lcd.write_string('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    grejac.on()
    ventilator.on()

    #Da pogasimo sve
    print("Gasi se sve za deset sekundi ne iskljucivati program")
    sleep(10)
    lcd.clear()
    grejac.off()
    ventilator.off()


else:
    print('Failed to get reading. Try again!')
