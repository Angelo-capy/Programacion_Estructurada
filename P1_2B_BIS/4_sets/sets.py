"""
Set es una coleccion desordenada, inmutable y no indexada.
No hay miembros duplicados.
"""

import os

os.system("cls")

personas = {"Ramiro", "Choche", "Lupe"}
print(personas)
personas.add("Peje")
print(personas)
personas.pop()
print(personas)
personas.clear()
print(personas)

os.system("cls")

varios = {3.12, 3, True, "hola"}
print(varios)

# ejemplo crear un programa que solicite los emails de los alumnos de la UTD.
# Almacenar en una lista y posteriormente mostrar en pantalla los mails sin duplicados

os.system("cls")

opc = "si"
email = []
while opc == "si":
    email.append(input("Dame el email: "))
    # print(email)
    opc = input("deseas solicitar otro email? (si/no) ").lower()

# imprimir los email sin duplicados

print(email)
