from Lector import captureRute
from Lector import parsexml
def menu():

    print("Practica 1")
    print("-----------------")
    print("1.- Cargar archivo")
    print("2.- Procesar archivo")
    print("3.- Escribir archivo de salida")
    print("4.- Mostrar datos del estudiante ")
    print("5.- Generar grafica")
    print("6.- Salir")
    opcion = input()
    return opcion

def menuP():
    while True:
        opcion = menu()
        if opcion == '1':
            parsexml(captureRute())


        #if opcion == '2':

        #if opcion == '3':

        #if opcion == '4':


        #if opcion == '5':


        if opcion == '6':
            print("KEVIN RAUL POZUELOS")
            print("CARNE: 201800992")
            print("Introduccion a la programacion y computacion 2 Seccion: ""A""")
            print("Ingenieria en Ciencias y Sistemas")
            print("4to Semestre")
            break
