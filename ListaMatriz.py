from Nodo import *
from Matriz import *

class ListaMatriz:
    def __init__(self):
        self.first = None



    def insert(self, nombre, n, m, dato):

        nuevo = Nodo(nombre, n, m, dato)
        if self.first is None:
            self.first = nuevo
        else:
            temp = self.first
            while temp.next is not None:
                temp = temp.next
            temp.next = nuevo
            nuevo.before = temp