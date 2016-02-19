nombre_archivo = raw_input("\n\nQue nombre deseas darle a tu archivo?: ")

nombre = nombre_archivo + ".txt"
archivo = open(nombre,"wb")
archivo.write ("Hola mundo")
archivo.close()

archivo = open(nombre,"r+")
hola = archivo.read()
print hola
archivo.close()