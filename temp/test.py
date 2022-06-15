#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  semafor.py
#  
#  Copyright 2022  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


# ~ def main(args):
    # ~ return 0

# ~ if __name__ == '__main__':
    # ~ import sys
    # ~ sys.exit(main(sys.argv))

#Ovde pocinje nas program
#Mogucnost da pokusamo da snimiimo o cemu se radi...
# nadam se da vidite sta zapravo kucam
# brze je i od klasicnih softvera za snimanje...

from gpiozero import LED
from gpiozero import Button
from time import sleep

zelena = LED(15)
zuta = LED(23)
crvena = LED(25)

btn = Button(21)

def ukljuci():
    zelena.on()
    zuta.on()
    crvena.on()

def iskljuci():
    zelena.off()
    zuta.off()
    crvena.off()

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
    

# ~ ukljuci()
# ~ sleep(5)
# ~ iskljuci()

# ~ while True:
    # ~ semafor()
    
def btn_press():
    
    btn.wait_for_press()
    # ~ blah = blah + 1
    # ~ print("Stisnuo si ", blah, " puta!!!")
    # ~ print("stisni")
    semafor()
    sleep(1)

#Ovo je test da vidimo kako ovo lepo snima...i da li lepo snima...
#hmmm malo vise baguje...ali posluzice da vidimo da li radi kako treba...
# mada kada krene onda radi....sada da zapocnemo
#ne pomaze nista ovo pomeranje rezolucije niti je skocniji ni to...nemam pojma...
# jedino ostaje regiju da snimam a to ce biti jos gore...
#ok ovo je test da vidimo kako ovo radi
while True:
    # ~ blah = 0
    btn_press()
    

