nombre_archivo = raw_input("\n\nQue nombre deseas darle a tu archivo?: ")

nombre = nombre_archivo + ".txt"
archivo = open(nombre,"w")
archivo.write('Hola mundo\n')
archivo.write('El nombre del archivo es: ' + nombre) 
archivo.close()

archivo = open(nombre,"r+")
hola = archivo.read()
print hola
archivo.close()