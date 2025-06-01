from paquete1 import modulo

print(modulo.saludar("Daniel Cerros"))

modulo.borrarPantalla()
nom, tel = modulo.solicitarDat2()
print(f"\n\t.:: Agenda Telefonica ::.\n\t\tNombre: {nom}\n\t\tTelefono:{tel}")
modulo.espereTecla()
