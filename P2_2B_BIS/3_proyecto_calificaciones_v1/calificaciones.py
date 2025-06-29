def borrarpantalla():
    """Function printing python version."""
    import os

    os.system("cls")


def esperartecla():
    """Function printing python version."""
    borrarpantalla()
    print("\U0001f552 Oprima cualquier tecla para continuar ...")
    input()


def menu_principal():
    print(
        "\n\t\t\t..::: \U0001f4c2 SISTEMA UTD\U0001f4c2 :::... \n\t\t..::: \U0001f4c2 Gestión de Calificaciones\U0001f4c2 :::...\n\n\t\t\t 1.- \U0001f4be Agregar  \n\t\t\t 2.- \U0001f50d Mostrar \n\t\t\t 3.- \U0001f501 Calcular promedios \n\t\t\t 4.- \U0001f464 SALIR "
    )
    opcion = input("\n\t\t\t \U0001f4dd Elige una opción (1-4): ").upper()
    return opcion


def agregar_calificaciones(lista):
    borrarpantalla()
    print("\U0001f4dd Agregar Calificaciones\U0001f4dd")
    nombre = input("\U0001f464 Nombre del Alumno: ").upper().strip()
    calificaciones = []
    for i in range(1, 4):
        continua = True
        while continua:
            try:
                cal = float(input(f"\U0001f4dd Calificacion del {i} parcial: "))
                if cal >= 0 and cal < 11:
                    calificaciones.append(cal)
                    continua = False
                else:
                    print("\U0001f4db Ingresa una calificacion valida\U0001f4db")
            except ValueError:
                print("\U0001f4dbIngresa un valor numerico\U0001f4db")
    lista.append([nombre] + calificaciones)
    print("ACCION REALIZADA CON EXITO!\U0001f389\U0001f389\U0001f389")


def mostrar_calificaciones(lista):
    borrarpantalla()
    print("\n\t.:: 🔍 Consultar Calificaciones 🔍::.\n")
    if len(lista) > 0:
        print(
            f"{'\U0001F464 Nombre':<15}{'\U0001F4DD Calf. 1':<10}{'\U0001F4DD Calf. 2':<10}{'\U0001F4DD Calf. 3':<10}"
        )
        print(f"{'-'*40}")
        for i in lista:
            print(f"{i[0]:<15}{i[1]:<10}{i[2]:<10}{i[3]:<10}")
            print(f"{'-'*40}")
            cuantos = len(lista)
            print(f"Son {cuantos} alumnos en la lista\U0001f4be")
    else:
        print("No hay calificaciones registradas en el sistema \U0001f4db")


# fila [1: ]     sum()   sum(fila[1:])
def calcular_promedios(lista):
    """Calcula el promedio de las calificaciones de cada alumno y el promedio grupal."""
    borrarpantalla()
    print("\n\t.:: \U0001f4be Calcular Promedio de un Alumno \U0001f4be ::.\n")
    if len(lista) > 0:
        print(f"{'\U0001F464 Alumno':<15}{'\U0001F4DD Promedio':<10}")
        print(f"{'-'*25}")
        promedio_grupal = 0
        for fila in lista:
            nombre = fila[0]
            promedio = sum(fila[1:]) / 3
            print(f"{nombre:<15}{promedio:<10.2f}")
            promedio_grupal += promedio
        print(f"{'-'*25}")
        promedio_grupal = promedio_grupal / len(lista)
        print(f"\U0001f4dd El promedio grupal es: {promedio_grupal:.2f}")
    else:
        print("No hay calificaciones registradas en el sistema \U0001f4db")

