import os
from typing import Iterable

os.system("cls")

###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")
for x in range(2, 21, 2):
    print(f"par: {x}")


# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")
suma = 0
for x in numeros:
    suma += x
media = suma/len(numeros)
print(f"La media es: {media}")

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")
maxi = 0
for n in numeros:
    if n > maxi:
        maxi = n
print(f"El numero mas grande es: {maxi}")


# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")
new_list = []
for n in palabras:
    if len(n) > 5:
        new_list.append(n)
print(new_list)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche", "arbol"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")
letra = input("Ingrese una letra: ")
cuenta = 0
for p in palabras:
    if p[0].lower() == letra.lower():
        cuenta += 1
print(f"El numero de palabras con es letra al inicio es: {cuenta}")