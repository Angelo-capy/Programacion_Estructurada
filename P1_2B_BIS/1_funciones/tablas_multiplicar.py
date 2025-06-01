"""
Crear un programa que calcule e imprima cualquier tabla de multiplicar

Requisitos:



"""

# version 2
# num = int(input("Dame el numero de la tabla a calcular: "))
# print(f"Tablas de multiplicar del {num}")
# for i in range(1, 11):
#    multi = num * i
#    print(f"{num} x {i}: {multi} ")

# version 3
# num = int(input("Dame el numero de la tabla a calcular: "))
# print(f"Tablas de multiplicar del {num}")
# i = 1
# while i <= 10:
#    multi = num * i
#    print(f"{num} x {i} = {multi}")
#    i += 1
#


def tablas_multiplicar(num):
    num = numero
    respuesta = ""
    for i in range(1, 11):
        multi = num * i
        respuesta += f"{num} x {i}: {multi}\n "
    return respuesta


numero = int(input("Dame el numero de la tabla a calcular: "))
print(f"Tablas de multiplicar del {numero}")

resultado = tablas_multiplicar(numero)
print(f"{resultado}")
