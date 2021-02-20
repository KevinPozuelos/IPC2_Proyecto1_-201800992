from Dato import *
class Matriz:
    def __init__(self):
        self.star = None


    def insert(self, x, y, dato):
        nuevo = Dato(x, y, dato)
        if self.star is None:
            self.star = nuevo
        else:
            temp = self.star
            while temp.next is not None:
                temp = temp.next
            temp.next = nuevo
