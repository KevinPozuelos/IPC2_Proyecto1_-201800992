from Matriz import *
class Nodo:
    def __init__(self, nombre, n,  m):
        self.nombre = nombre
        self.n = n
        self.m = m
        self.next = None
        self.before = None
        self.matriz = Matriz()
        self.reducida = Matriz()


    def getMatriz(self):
        self.matriz.mostrar()