from Nodo import *
from Matriz import *

class ListaMatriz:
    def __init__(self):
        self.first = None

    def insert(self, nombre, n, m):

        nuevo = Nodo(nombre, n, m)
        if self.first is None:
            self.first = nuevo
            return nuevo
        else:
            temp = self.first
            while temp.next is not None:
                temp = temp.next
            temp.next = nuevo
            nuevo.before = temp
            return nuevo
        return None

    def mostrar(self):
        tmp = self.first
        contador = 1
        while tmp is not None:
            print(str(contador) + '. nombre: ' + str(tmp.nombre) + ', n = ' + str(tmp.n) + ' m = ' + str(tmp.m))
            print(tmp.matriz.mostrar())

            contador += 1
            tmp = tmp.next

    def getSize(self):
        tmp = self.star
        cont = 0
        while tmp is not None:
            cont += 1
            tmp = tmp.next
        return cont


