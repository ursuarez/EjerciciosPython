#!/usr/bin/env python
# -*-coding:utf-8-*-

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return '\n  Mi nombre es %s.' % self.nombre


class Estudiante(Persona):
    def __init__(self, nombre, edad, escuela):
        Persona.__init__(self, nombre, edad)
        self.escuela = escuela

    def get_escuela(self):
        return '\n  Yo estudio en %s.' % self.escuela

e = Estudiante('Ricardo', 21, 'UPIICSA')

print e.saludar()
print e.get_escuela()