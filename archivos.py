archivo = open("foo.txt","wb")
archivo.write ("Hola mundo")
archivo.close()

archivo = open("foo.txt","r+")
hola = archivo.read()
print hola
archivo.close()