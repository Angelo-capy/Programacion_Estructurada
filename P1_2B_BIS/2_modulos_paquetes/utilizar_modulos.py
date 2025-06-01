# 1er forma de utilizar los modulos

import modulo

modulo.borrarPantalla()
print(modulo.saludar("Angel Franco"))

# 2da forma de utilizar modulos

from modulo import saludar, borrarPantalla

borrarPantalla()
print(saludar("dan ortega"))

nombre = input("ingresa el nombre del contacto: ")
telefono = input("Ingresa su numero de telefono: ")
nom, tel = modulo.solicitarDatillo4(nombre, telefono)
print(f"\tNombre completo: {nom}\n\tTelefono: {tel}")
