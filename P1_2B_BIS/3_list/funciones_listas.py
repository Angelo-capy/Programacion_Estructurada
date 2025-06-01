"""
List(Array)
son colecciones o conjuntos de datos/valores bajo un mismo nombre,
para acceder a los valores se hace un indice numerico

Nota: sus valores si son modificables

la lista es una coleccion ordenada y modificable. Permite
miembros duplicados


"""

import os

os.system("cls")

# Funciones mas comunes en las listas

paises = ["Mexico", "Brasil", "Spain", "Canada"]

numeros = [23, 12, 100, 34]

# Ordenar ascendentemente
print(numeros)
numeros.sort()
print(numeros)
print(paises)
paises.sort()
print(paises)

# Ingresar o insertar o agregar elementos a una lista


# 1er forma
paises.append("Honduras")
# 2da forma
paises.insert(1, "Honduras")
print(paises)

# Eliminar o borrar o quitar elementos a una lista
# 1er forma
paises.pop(1)
print(paises)
# 2da forma
paises.remove("Honduras")
print(paises)

# Buscar un elemento dentro de la lista
# 1er forma
resp = "Brasil" in paises
if resp:
    print("Pais encontrado")
else:
    print("No se encontro el pais")

# 2da forma
pais_buscar = input("Dame el pais: ")
for i in range(0, len(paises)):
    if paises[i] == pais_buscar:
        print("Pais encontrado")
    else:
        print("No se encontro el pais")

os.system("cls")

# cuantas veces aparece un elemento dentro de una lista

# numeros = [23, 12, 100, 34]

numeros.append(12)

print(f"el numero numero 12 aparece: {numeros.count(12)} veces")

# Identificar o conocer el valor del indice de un valor

# paises = ["Mexico", "Brasil", "Spain", "Canada"]

Indice = paises.index("Spain")
print(Indice)
paises.pop(Indice)
print(paises)

# Recorrer los valores de una lista

for i in paises:
    print(i)

# 2da forma
for i in range(0, len(paises)):
    print(f"El valor de {i} es: {paises[i]}")


# Unir contenido de listas

print(paises)
print(numeros)
paises.extend(numeros)
print(paises)
