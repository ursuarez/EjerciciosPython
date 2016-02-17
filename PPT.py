#!/usr/bin/env python
# -*-coding:utf-8-*-

import time
from time import sleep
import random

sus = "-" * 35
cage = ["piedra","papel","tijera"]

while True:
	eleccion = raw_input("\nSelecciona una opcion [piedra, papel o tijera] : ")
	if eleccion not in cage:
		print "\nNo hagas trampa!"
		continue

	pc = random.choice(cage)
	sleep(0.5)
	print(("\nLa Computadora eligio {}.").format(pc))
	if eleccion == pc:
		print "\n         EMPATE."
	elif eleccion == "piedra" and pc == "tijera":
		print "\n         GANASTE!"
	elif eleccion == "papel" and pc == "piedra":
		print "\n         GANASTE!"
	elif eleccion == "tijera" and pc == "papel":
		print "\n         GANASTE!"
	else:
		print "\n         PERDISTE :("
	print "\n", sus, "\n"

