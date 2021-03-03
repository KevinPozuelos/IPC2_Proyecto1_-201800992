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

    def getNodo(self, siguiente, m, inicio):
        tmp = inicio        #lista que nos servira como auxiliar para hacer la comparacion
        aux = siguiente     #fila que vamos a comparar
        i = 1              #variable que nos ayudara a manejar las columnas para encontrar y validar patron
        listaFilas = ""     #variable donde se agregaran las filas a reducir, primer dato es fila pivote

        while tmp is not None:
            
            if aux.x != tmp.x and aux.y == tmp.y and aux.accessM == tmp.accessM:    #verificamos que no se compare la misma fila  que se desea comparar y se verifica datos de acceso
                if i == int(m): #si i = al numero de columnas de la matriz, el patron de la fila es correcto
                    if listaFilas != "":
                        listaFilas += ',' + tmp.x
                    else:
                        listaFilas = aux.x + ',' + tmp.x

                    i = 1
                    aux = siguiente
            
                aux = aux.next
                i += 1
            
            if i != int(m) and str(i) != tmp.y:     #Si una columna coincide pero las demas no y comienza nueva fila, se reinician variables de fila a buscar y manejador de columna para la fila siguiente a comparar
                auxSiguiente = tmp.next
                if auxSiguiente != None:
                    if auxSiguiente.x != tmp.x:
                        i = 1
                        aux = siguiente
            tmp = tmp.next


        return listaFilas

    def sumaM(self, fila, m, matriz, inicio):
        tmp = self.star


    def getValue1(self, x, y):

        tmp = self.star
        contador = 0
        while tmp is not None:
            if int(tmp.x) == int(x) and int(tmp.y) == int(y):
                return tmp.value
            tmp = tmp.next
        return None

    def mostrar(self):
        tmp = self.star
        contador = 1
        while tmp is not None:
            print(
                str(contador) + '. Coordenada x : ' + str(tmp.x) + ', Coordenada y : ' + str(tmp.y) + ', Valor ,' + str(
                    tmp.value) + ' Matriz-patron: ' + str(tmp.accessM))
            contador += 1
            tmp = tmp.next



