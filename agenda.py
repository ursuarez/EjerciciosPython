#!/usr/bin/env python
# -*-coding:utf-8-*-

from time import sleep

numero_contactos = input("\n\n\n\nCuantos contactos desea agregar?: ")
nombre_archivo = raw_input("\nQue nombre desea darle a su archivo?: ")

nombre = nombre_archivo + ".txt"
archivo = open(nombre, "w")
archivo.write('\t' + nombre_archivo.upper())

sus = "-" * 35

for contador in range(numero_contactos):
    num_contador = contador + 1
    print "\n", sus, "\n"
    archivo.write('\n\n' + sus + '\n\n')

    print "Contacto #%d : \n" % num_contador
    archivo.write('Contacto # ' + str(num_contador) + '\n')

    nombre = raw_input("\nNombre: ")
    archivo.write('\nNombre: ' + nombre)

    apellidop = raw_input("\nApellido Paterno: ")
    archivo.write('\nApellido Paterno: ' + apellidop)

    apellidom = raw_input("\nApellido Materno: ")
    archivo.write('\nApellido Materno: ' + apellidom)

    telefono = raw_input("\nTel: ")
    archivo.write('\nTel: ' + telefono)

    Email = raw_input("\nEmail: ")
    archivo.write('\nEmail: ' + Email)


print "\n\nGuardando archivo "

for cont in range(3):
	print ". " 
	sleep(0.5)
archivo.close()