# Un modulo es simplemente un archivo con extension .py que
# contiene un codigo de python (Funciones, clases, variables, etc.).

# Un paquete es una carpeta que contiene varios modulos
# (Archivos ,py) y un archivo especial llamado __init__.py, que
# le indica a python que esa carpeta debe tratarse como un paquete.

import os


# caso 1: Funcion que no recibe parametros y no regresa valor
def solicitarDatos1():
    nombre = input("Nombre: ")
    tel = input("Telefono: ")

    print(f"Soy funcion 1, Tu nombre es: {nombre} y tu telefono es: {tel}")


# caso 3 Funcion que recibe parametros y no regresa valor
def solicitarData3(nombre, tel):
    nom = nombre
    telefono = tel
    print(f"Soy funcion 3, Tu nombre es: {nom} y tu telefono es: {telefono}")


# caso 2: Funcion que no recibe parametros y regresa valor
def solicitarDat2():
    nombre = input("Nombre: ")
    tel = input("Telefono: ")
    return nombre, tel


# caso 4: Funcion que recibe parametros y regresa valor
def solicitarDatillo4(nombre, tel):
    nom = nombre
    telefono = tel
    return nom, telefono


def borrarPantalla():
    os.system("cls")


def espereTecla():
    input("... Oprima una tecla para continuar ... ")


def saludar(nombre):
    nom = nombre
    return f"\tHola, bienvenido: {nom}\n"
