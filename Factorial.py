"""
		FACTORIAL
"""

numero = input("\n\nIngrese el numero del cual quiere saber su factorial: ")
acumulador = 1

while numero > 0:
	acumulador = numero * acumulador
	numero = numero - 1

print "\nEl factorial es: %i" %acumulador


