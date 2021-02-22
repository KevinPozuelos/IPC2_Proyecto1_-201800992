import xml.etree.ElementTree as ET
from Matriz import *
from ListaMatriz import *


ListaMtx = ListaMatriz()
def captureRute():
    rute = input("Ingrese nombre del archivo: ")


    return rute

def parsexml(rute):
    tree = ET.parse(rute)
    root = tree.getroot()
    for element in root:

        Mtx = Matriz()

        ListaMtx.insert(element.attrib['nombre'], element.attrib['n'], element.attrib['m'], Mtx)
        for subelement in element:
            if subelement.text != '0':
                Mtx.insert(subelement.attrib['x'], subelement.attrib['y'], subelement.text, 1)
            else:
                Mtx.insert(subelement.attrib['x'], subelement.attrib['y'], subelement.text, 0)






    ListaMtx.mostrar()