from Nodo import *
from Matriz import *

class ListaMatriz:
    def __init__(self):
        self.first = None



    def insert(self, nombre, n, m, dato, accessM):

        nuevo = Nodo(nombre, n, m, dato, accessM)
        if self.first is None:
            self.first = nuevo
        else:
            temp = self.first
            while temp.next is not None:
                temp = temp.next
            temp.next = nuevo
            nuevo.before = temp

    def mostrar(self):
        tmp = self.first
        contador = 1
        while tmp is not None:
            print(str(contador) + '. nombre: ' + str(tmp.nombre) + ', n = ' + str(tmp.n) + ' m = ' + str(tmp.m))
            print(str(tmp.dato.mostrar()))
            print(str(tmp.accessM.mostrar()))
            contador += 1
            tmp = tmp.next

    def getSize(self):
        tmp = self.inicio
        cont = 0
        while tmp is not None:
            cont += 1
            tmp = tmp.next
        return cont