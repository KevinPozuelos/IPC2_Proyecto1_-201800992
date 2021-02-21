import xml.etree.ElementTree as ET
from Matriz import *
from ListaMatriz import *

Mtx = Matriz()
ListaMtx = ListaMatriz()
def captureRute():
    rute = input("Ingrese nombre del archivo")


    return rute

def parsexml(rute):
    tree = ET.parse(rute)
    root = tree.getroot()
    for element in root:
        print(element.attrib['nombre'], element.attrib['n'], element.attrib['m'])
        #ListaMtx.insert(element.attrib['nombre'], element.attrib['n'], element.attrib['m'], Mtx)
        for subelement in element:
            print("Valor: " + subelement.text, "cordenada x: " + subelement.attrib['x'], "cordenada y: " + subelement.attrib['y'])
            #Mtx.insert(subelement.text, subelement.attrib['x'], subelement.attrib['y'])
