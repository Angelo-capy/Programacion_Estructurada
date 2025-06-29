# Crear un proyeto que permita gestionar (administrar) calificaciones, colocar un menu de opciones
# para agregar, eliminar, mostrar, calcular promedio de calificaciones de un estudiante
# Notas:
# 1.- Utilizar funciones y mandar llamar desde otro archivo (modulos)
# 2.- Utilizar list (bidimensional) para almacenar los siguientes atributos:
# el nombre del alumno asi como sus tres calificaciones


import calificaciones


def main():
    datos = []

    opcion = True
    while opcion:
        calificaciones.borrarpantalla()
        opcion = calificaciones.menu_principal()

        match opcion:
            case "1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperartecla()
            case "2":
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperartecla()
            case "3":
                calificaciones.calcular_promedios(datos)
                calificaciones.esperartecla()
            case "4":
                opcion = False
                calificaciones.borrarpantalla()
                print("\u2705 Terminaste la ejecucion del SW \u2705")

            case _:
                calificaciones.borrarpantalla()
                input("\n\t\u274c Opción invalida vuelva a intentarlo ... ")


if __name__ == "__main__":
    main()
