"""Module providing a function printing python version."""

# Lista para almacenar múltiples películas
peliculas = []

# Diccionario para almacenar los atributos de UNA película
pelicula = {}

import os


def borrarpantalla():
    os.system("cls")  # En Windows, el comando correcto es "cls"


def esperartecla():
    input("\t Oprima cualquier tecla para continuar ...")
    borrarpantalla()


def crearPeliculas():
    borrarpantalla()
    print("\n\t.::📝 Alta de Películas 📝::. ")
    pelicula.update({"nombre": input("INGRESA EL NOMBRE: ").upper().strip()})
    pelicula.update({"categoria": input("INGRESA LA CATEGORIA: ").upper().strip()})
    pelicula.update(
        {"clasificacion": input("INGRESA LA CLASIFICACION: ").upper().strip()}
    )
    pelicula.update({"genero": input("INGRESA EL GENERO: ").upper().strip()})
    pelicula.update({"idioma": input("INGRESA EL IDIOMA: ").upper().strip()})
    input("\n\t\t ✅ LA OPERACIÓN SE REALIZÓ CON ÉXITO ✅")


def borrarPeliculas():
    borrarpantalla()
    print("\n\t.::📚 Borrar TODAS las Películas 📚::.\n")
    resp = input("📚 ¿Deseas quitar todas las películas del sistema? (Si/No): ").lower()
    if resp == "si":
        pelicula.clear()
        input("\n\t\t ✅ LA OPERACIÓN SE REALIZÓ CON ÉXITO ✅")


def mostrarPeliculas():
    borrarpantalla()
    print("\n\t.:: 🔍 Consultar Película 🔍::.\n")
    if len(pelicula) > 0:
        for clave, valor in pelicula.items():
            print(f"\t{clave.capitalize()} : {valor}")
    else:
        print("\t ⚠️ No hay películas en el sistema ⚠️")


def agregarCaracteristicaPeliculas():
    borrarpantalla()
    print("\n\t.:: 📝 Agregar Característica a Película 📝::.\n")
    atributo = input("Ingresa la nueva característica: ").lower().strip()
    valor = input("📝 Ingresa el valor de la característica: ").upper().strip()
    pelicula.update({atributo: valor})
    input("\n\t\t ✅ CARACTERÍSTICA AGREGADA CON ÉXITO ✅")


def modificarCaracteristicasPeliculas():
    borrarpantalla()
    print("\n\t.:: 🔄 Modificar Características de Película 🔄::.\n")
    if len(pelicula) > 0:
        for clave in list(pelicula.keys()):
            print(f"\t{clave} : {pelicula[clave]}")
            resp = input(f"\t¿Deseas cambiar el valor de '{clave}'? (Si/No): ").lower()
            if resp == "si":
                nuevo_valor = input("\t🔁 Nuevo valor: ").upper().strip()
                pelicula.update({clave: nuevo_valor})
        print("\n\t\t ✅ CAMBIOS REALIZADOS CON ÉXITO ✅")
    else:
        print("\t ⚠️ No hay películas en el sistema ⚠️")
    esperartecla()


def borrarCaracteristicaPeliculas():
    borrarpantalla()
    print("\n\t.:: 🗑️ Borrar Característica de Película 🗑️::.\n")
    if len(pelicula) > 0:
        print("\n\tCaracterísticas actuales:")
        for clave, valor in pelicula.items():
            print(f"\t{clave} : {valor}")
        resp = input("\n\t¿Deseas borrar una característica? (Si/No): ").lower()
        if resp == "si":
            atributo = input("Nombre de la característica a borrar: ").lower().strip()
            if atributo in pelicula:
                pelicula.pop(atributo)
                print("\n\t\t ✅ CARACTERÍSTICA BORRADA CON ÉXITO ✅")
            else:
                print(f"\n\t⚠️ La característica '{atributo}' no existe.")
    else:
        print("\t⚠️ No hay películas en el sistema ⚠️")
    esperartecla()
