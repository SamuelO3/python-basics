import os
from typing import Iterable

os.system("cls")

###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")
for n in range(1, 20 + 1):
    if n % 2 == 0:
        print(n)


# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")

media = 0
for index, n in enumerate(numeros):
    media += n
    if index == len(numeros) - 1:
        print(media / 2)

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")
mayor = numeros[0]
lenght_numeros = len(numeros)
for i in range(lenght_numeros):
    if numeros[i] > mayor:
        mayor = numeros[i]
print(mayor)


# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")
palabras_5_letras = [p for p in palabras if len(p) > 5]
print(palabras_5_letras)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")

letra = input("Ingrese una letra: ")
contador = 0
for p in palabras:
    if p[0] == letra:
        contador += 1
print(f"Numero de letras: {contador}")
