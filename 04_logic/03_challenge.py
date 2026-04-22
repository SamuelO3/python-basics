"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices.
Si no existe tal combinación, devuelve None.

numeros = [4, 5, 6, 2]
objective = 8

find_first_sum(nums, goal)  # [2, 3]
"""

import operator
import os

os.system("cls")


numeros = [4, 5, 6, 4, 2]
objective = 8


def find_first_sum_list(numeros: list[int], objective: int) -> list[int]:
    """
    Encuantra los primeros numeros del array que sument un numero goal y devulve sus indices.

    Args:
        numeros (list[int]): arreglo de numeros donde buscaremos la pareja
        goal (int): numero objetivo de la suma

    Return:
        [numero_1, numero_2] (list[int]):lista con indices de los numeros de la pareja
        Si no existe una suma que de la meta retorna None
    """

    lenght = len(numeros)

    for i in range(lenght):
        for j in range(i + 1, lenght):
            if numeros[i] + numeros[j] == objective:
                return [i, j]

    return None


print("Con fors anidados", find_first_sum_list(numeros=numeros, objective=objective))


def find_first_sum_dict(numeros: list[int], objective: int) -> list[int]:
    """
    Encuantra los primeros numeros del array que sument un numero goal y devulve sus indices.

    Args:
        numeros (list[int]): arreglo de numeros donde buscaremos la pareja
        goal (int): numero objetivo de la suma

    Return:
        [numero_1, numero_2] (list[int]):lista con indices de los numeros de la pareja
        Si no existe una suma que de la meta retorna None
    """

    progress = {}

    for index, num in enumerate(numeros):
        if num in progress:
            continue

        dif = objective - num

        if dif in progress:
            return [progress[dif], index]

        progress[num] = index

    return None


print("Con diccionario", find_first_sum_dict(numeros=numeros, objective=objective))
