"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices.
Si no existe tal combinación, devuelve None.

numeros = [4, 5, 6, 2]
objective = 8

find_first_sum(nums, goal)  # [2, 3]
"""

import os

os.system("cls")


numeros = [4, 5, 6, 4, 2]
objective = 7


def find_first_sum(nums: list[int], goal: int) -> list[int]:
    """
    Encuentra dos numeros que sumados den un numero meta

    Args:
        nums(list[int]): arreglo de numeros para buscar la suma
        goal(int): numero meta

    Returns:
        tuple: tuple con el indice de los numeros que sumados dan la meta
    """

    progress: dict[int, int] = {}

    for i, n in enumerate(nums):
        resto: int = goal - n

        if resto in progress:
            return [progress[resto], i]
        progress[n] = i  

print(find_first_sum(numeros, objective))


def find_first_sum_for(nums: list[int], goal: int) -> list[int]:
    """
    Encuentra dos numeros que sumados den un numero meta

    Args:
        nums(list[int]): arreglo de numeros para buscar la suma
        goal(int): numero meta

    Returns:
        tuple: tuple con el indice de los numeros que sumados dan la meta
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == goal:
                return[i, j]
            

print(find_first_sum_for(numeros, objective))