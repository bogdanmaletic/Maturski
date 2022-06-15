#Ovaj program sluzi za testiranje RPLCD biblioteke
#LCD testiramo sa sudo rplcd-tests gpio testsuite mode=BOARD cols=16 rows=2 rs=15 e=16 data=21,22,23,24 charmap=A02
#Za i2c ide rplcd-tests i2c testsuite expander=PCF8574 addr=27 port=1 cols=16 rows=2 charmpap=A02

#Ovaj sluzi za inicijalizaciju
from signal import pause
# from RPLCD.gpio import CharLCD
from RPLCD.i2c import CharLCD
from RPi import GPIO
from time import sleep

# na kraju da vidimo kako radi
# lcd = CharLCD(pin_rs=15, pin_rw=18, pin_e=16, pins_data=[21, 22, 23, 24],
#               numbering_mode=GPIO.BOARD,
#               cols=20, rows=4, dotsize=8,
#               charmap='A02',
#               auto_linebreaks=True)

#Ovaj je za nas slucaj..u originalu 21 22 23 24, rw = 18 charmap='A02',
# GPIO.cleanup()
GPIO.setwarning = False
print("Verizija je :",GPIO.VERSION)

#Ovo je GPIO verzija
# lcd = CharLCD(pin_rs=15, pin_e=16, pins_data=[21, 22, 23, 24],
#               numbering_mode=GPIO.BOARD,
#               cols=16, rows=2, dotsize=8,
#               charmap='A02',
#               auto_linebreaks=True,
#               compat_mode=True)

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)

# lcd.clear()
# lcd.home()
# lcd.cursor_mode = 'blink'
# lcd.write_string("OOO zdravo\r\n Helooo world")
lcd.clear()

lcd.write_string('Ciscenje displeja :)')
# lcd.write_string('hellooo')
# tepmStr = 'Vidi radi'
# lcd.write_string(tepmStr.encode('utf-8'))
sleep(1)
# lcd.write_string('Hello world')
# lcd.cursor_pos = (1,0)
# lcd.write_string('Ok')
# pause()
# print(lcd.pins)
print("ovo je posle pauze")
# sleep(3)
# lcd.pins()
lcd.clear()
# lcd.close(clear=True)
lcd.close(clear=True)
print("Done...")
# GPIO.cleanup()
quit()

