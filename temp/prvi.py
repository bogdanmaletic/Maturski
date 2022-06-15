from gpiozero import LED
from time import sleep

#led = LED(18)

#postavljamo zelenu diodu na GPIO15
zelena = LED(15)
#zuta na GPIO23
zuta = LED(23)
#crvena na GPIO25
crvena = LED(25)

def ukljuci():
	"""Funkcija koja ukljucuje diode u ovom programu"""
	zelena.on()
	zuta.on()
	crvena.on()
	
def iskljuci():
	zelena.off()
	zuta.off()
	crvena.off()
	
def jednostavno():
	ukljuci()
	sleep(1)
	iskljuci()
	sleep(1)
	
def semafor():
	#crvena osam sekundi
	crvena.on()
	sleep(8)
	zuta.on()
	sleep(2)
	crvena.off()
	zuta.off()
	zelena.on()
	sleep(7)
	zelena.off()
	#sada blinka zeleno ima pola sekunde pauze
	sleep(0.5)
	zelena.on()
	sleep(0.5)
	zelena.off()
	print("zeleno prvi put")
	sleep(0.5)
	zelena.on()
	sleep(0.5)
	zelena.off()
	print("zeleno drugi put")
	sleep(0.5)
	zelena.on()
	sleep(0.5)
	print("zeleno drugi put")
	zelena.off()
	sleep(0.5)
	#sada zuta 2 sekunde
	zuta.on()
	sleep(2)
	zuta.off()

#while True:
	#ovo bilo ranije
	#led.on()
	#sleep(1)
	#led.off()
	#sleep(1)
	
	#ukljuci()
	
	#sleep(5)
	
	#iskljuci()
	
	#crvena.on()
	#zuta.on()
	#zelena.on()
	
	#sleep(5)
	
	#crvena.off()
	#zelena.off()
	#zuta.off()
	
#	crvena.blink()
#	sleep(1)

while True:
	semafor()
	

