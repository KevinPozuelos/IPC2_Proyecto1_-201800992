from Dato import *


class Matriz:
    def __init__(self):
        self.star = None

    def insert(self, x, y, dato, accessM):
        nuevo = Dato(x, y, dato, accessM)
        if self.star is None:
            self.star = nuevo
        else:
            temp = self.star
            while temp.next is not None:
                temp = temp.next
            temp.next = nuevo

    def mostrar(self):
        tmp = self.star
        contador = 1
        while tmp is not None:
            print(
                str(contador) + '. Coordenada x : ' + str(tmp.x) + ', Coordenada y : ' + str(tmp.y) + ', Valor ,' + str(
                    tmp.value) + ' Matriz-patron: ' + str(tmp.accessM))
            contador += 1
            tmp = tmp.next

    def reducir(self):
        tmp = self.star
        contador = 1

