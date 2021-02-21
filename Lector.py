import xml.etree.ElementTree as ET

from ListaMatriz import *


ListaMtx = ListaMatriz()

def captureRute():
    rute = input("Ingrese nombre del archivo: ")


    return rute

def parsexml(rute):
    tree = ET.parse(rute)
    root = tree.getroot()
    for element in root:
        accessM = Matriz()
        Mtx = Matriz()

        ListaMtx.insert(element.attrib['nombre'], element.attrib['n'], element.attrib['m'], Mtx, accessM)
        for subelement in element:

            Mtx.insert(subelement.attrib['x'], subelement.attrib['y'], subelement.text)
            if subelement.text != '0':
                accessM.insert(subelement.attrib['x'], subelement.attrib['y'], str(1))
            else:
                accessM.insert(subelement.attrib['x'], subelement.attrib['y'], str(0))




    ListaMtx.mostrar()