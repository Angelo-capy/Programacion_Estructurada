"""Una funcion es un conjunto de estrucciones agrupadas bajo un nombre en particular como un programa mas peque
que cumple con una funcion especifica. La funcion se puede reutiilizar con el simple hecho de invocarla es
decir mandarla a llamar

Sintaxis:

    def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

      nombredeMifuncion(parametros)

    Las funciones pueden ser de cuatro tipos

     Funciones de tipo "Procedimiento"
     1.- Funcion que no recibe parametros y no regresa valor
     3.- Funcion que recibe parametros y no regresa valor

     Funciones de tipo "Funcion"
     2.- Funcion que no recibe parametros y regresa valor
     4.- Funcion que recibe parametros y regresa valor

"""


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


# Llamar mis funciones:
# caso1
solicitarDatos1()

# caso3
nom3 = input("Nombre: ")
tel3 = input("Telefono: ")
solicitarData3(nom3, tel3)

# caso2
nom2, tel2 = solicitarDat2()
print(f"nombre: {nom2} \n telefono: {tel2}")

# caso4
nom4 = input("nombre: ")
tel4 = input("telefono: ")
nombre4, telefono4 = solicitarDatillo4(nom4, tel4)
print(f"Nombre: {nombre4} \n telefono: {telefono4}")
