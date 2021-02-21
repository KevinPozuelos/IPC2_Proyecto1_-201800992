from Dato import *
class Nodo:
    def __init__(self, nombre, n, m, dato, accessM):
        self.nombre = nombre
        self.n = n
        self.m = m
        self.dato = dato
        self.next = None
        self.before = None
        self.accessM = accessM