#!/usr/bin/env python
# -*-coding:utf-8-*-

class Persona(object): # object es optativo
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        texto = "Mi monbre es: {} y tengo {} años"
        return (texto).format(self.nombre, self.edad)

class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        self.curso = curso
        super(Estudiante,self).__init__(nombre, edad)

    def __str__(self):
        texto = "Mi nonbre es: {}, tengo {} años y curso {}"
        return (texto).format(self.nombre, self.edad, self.curso)

p = Persona("Ricardo", 21)
e = Estudiante("Ricardo", 21, "Python")
print p
print e
