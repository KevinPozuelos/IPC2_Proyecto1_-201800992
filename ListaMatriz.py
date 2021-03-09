from Nodo import *
import os

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
        tmp = self.first
        cont = 0
        while tmp is not None:
            cont += 1
            tmp = tmp.next
        return cont


    def reducir(self):

        tmp = self.first
        filaVeri = ""
        nextFila = ""

        while tmp is not None:
            matriz = tmp.matriz.star

            while matriz is not None:

                if filaVeri.find(matriz.x) == -1:   #Se verifica que la fila no se haya analizado
                    
                    nextFila = tmp.matriz.getNodo(matriz, tmp.m, tmp.matriz.star)

                    if nextFila != "":
                        if filaVeri != "":
                            filaVeri += ';' + nextFila
                        else:
                            filaVeri = nextFila

                matriz = matriz.next
            print("Nombre matriz : " + tmp.nombre + " -- Reducciones: " + filaVeri)

            filaVeri = ""
            tmp = tmp.next


    def suma(self, matriz, listafila):
        tmp = self.first
        matriz = tmp.matriz.star
        #while matriz is not None:



    def graph(self, matrix, busqueda):
        encontrado = True
        tmp = matrix.first
        dot = "digraph G { \n"
        while tmp is not None and encontrado:
            if str.lower(tmp.nombre) == str.lower(busqueda):
                lista = tmp.matriz.star
                while lista is not None:
                    if lista.x == "1":
                        if lista.y == "1":
                            dot += "Inicio[label=\"Matrices\"]\n"
                            dot += "Matriz[label=\"" + tmp.nombre + "\"]\n"
                            dot += "filas[label=\" n = " + tmp.n + "\", shape = doublecircle, color = blue]\n"
                            dot += "columnas[label=\" m = " + tmp.m + "\", shape = doublecircle, color = blue]\n"
                            dot += "Inicio -> Matriz \n"
                            dot += "Matriz -> filas\n"
                            dot += "Matriz -> columnas\n"
                        nodo = "fila1" + lista.y
                        dot += nodo + "[label=\"" + lista.value + "\"]\n"
                        dot += "Matriz" + " -> " + nodo + "\n"
                    else:
                        nodoAnterior = "fila" + str(int(lista.x)-1) + lista.y
                        nodo = "fila" + lista.x + lista.y
                        dot += nodo + "[label=\"" + lista.value + "\"]\n"
                        dot += nodoAnterior + " -> " + nodo + "\n"
                    lista = lista.next
                encontrado = False
            tmp = tmp.next
        
        try:
            dot += "}"
            archivo = open("grafico.dot", 'w')
            archivo.write(dot)
            archivo.close()

            os.system("dot -Tpng grafico.dot -o grafico.png")
            os.startfile("grafico.png")
        except Exception:
            if not encontrado:
                return False

    def getNodo(self, valor):
        tmp = self.first
        while tmp is not None:
            if str.lower(tmp.nombre) == str.lower(valor):
                return tmp
            tmp = tmp.next
        return None

    def mostrarnom(self):
        tmp = self.first
        contador = 1
        while tmp is not None:
            print(str(contador) + '. nombre: ' + str(tmp.nombre))


            contador += 1
            tmp = tmp.next