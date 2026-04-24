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


def carnivore_egg_counter(egg_list: list[int]):
    """
    Calcula el numero de huevos carnivoros (pares)

    Args:
        egg_list (list[int]): lista de huevos a calcular

    Returns:
        suma de huevos carnivoros calculados (pares)
    """

    carnivore = 0

    for n in egg_list:
        if n % 2 == 0:
            carnivore += abs(n)

    return carnivore


print(carnivore_egg_counter(list(range(0, 5))))
print(carnivore_egg_counter(list(range(1, 2))))
print(carnivore_egg_counter(list(range(-2, 10))))
