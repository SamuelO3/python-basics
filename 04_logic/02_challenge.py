"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos.
Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros
(es decir, la suma de todos los números pares en la lista).
"""

from os import system

if system("clear") != 0:
    system("cls")


def carnivore_egg_counter(egg_list: list[int]) -> int:
    """
    Esta funcion recibe una lista de numeros enteros y calcula cuantos huevos hay en la lista

    Args:
        egg_list (list[int]): lista de numeros donde buscaremos

    Return:
        total de pares en el arreglo, 0 si no hay pares
    """

    egg_counter = 0

    for n in egg_list:
        if n % 2 == 0:
            egg_counter += n

    egg_counter = sum(filter(lambda x: x % 2 == 0, egg_list))

    return egg_counter

print(carnivore_egg_counter(list(range(1, 11))))
print(carnivore_egg_counter(list(range(1, 11, 2))))
print(carnivore_egg_counter(list(range(-10, 0))))
print(carnivore_egg_counter(list(range(-11, 0, 2))))