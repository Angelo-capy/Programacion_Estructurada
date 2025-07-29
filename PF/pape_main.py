import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from funciones import borrarpantalla, esperartecla
from inventario.inventario import agregarinventario, consultarinventario
from ventas.venta import hacer_venta, historial_movimientos
from usuarios.usuario import iniciar_sesion, insertar_usuario

def menu_usuarios():
    while True:
        borrarpantalla()
        print("\n🖋️ BIENVENIDO A PAPELERÍA DEL NORTE")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            usuario = iniciar_sesion()
            if usuario:
                menu_principal(usuario)
        elif opcion == "2":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo: ")
            contrasena = input("Contraseña: ")
            celular = input("Celular: ")
            insertar_usuario(nombre, apellido, correo, contrasena, celular)
            esperartecla()
        elif opcion == "3":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida.")
            esperartecla()


def menu_principal(usuario):
    while True:
        borrarpantalla()
        print(f"\n📋 Sesión activa como: {usuario['nombre']} ({usuario['correo_electronico']})")
        print("1. Agregar al inventario")
        print("2. Hacer una venta")
        print("3. Mostrar inventario")
        print("4. Ver historial de movimientos")
        print("5. Cerrar sesión")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                agregarinventario()
                esperartecla()
            case "2":
                hacer_venta(usuario['id_usuario'])
                esperartecla()
            case "3":
                consultarinventario()
                esperartecla()
            case "4":
                historial_movimientos()
                esperartecla()
            case "5":
                print("👋 Sesión cerrada.")
                break
            case _:
                print("❌ Opción inválida.")
                esperartecla()


if __name__ == "__main__":
    menu_usuarios()
