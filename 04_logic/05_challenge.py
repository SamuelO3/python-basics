"""
Tienes dos listas de números, lista_a y lista_b, ambas de la misma longitud.

Cada número en lista_a se "enfrenta" al número en la misma posición en lista_b.

- Si el número en lista_a es mayor, su valor se suma al siguiente número en lista_a.
- Si el número en lista_b es mayor, su valor se suma al siguiente número en lista_b.
- Si los dos números son iguales, ambos se eliminan y no afectan al siguiente par.

Debes simular estos enfrentamientos y devolver el resultado final:
- Si al final queda un número en lista_a, devuelve ese número seguido de la letra "a" (por ejemplo, "3a").
- Si al final queda un número en lista_b, devuelve ese número seguido de la letra "b" (por ejemplo, "2b").
- En caso de empate, devuelve la letra "x".

lista_a = [2, 4, 2]
lista_b = [3, 3, 4]

resultado = battle(lista_a, lista_b)  # -> "2b"

# Explicación:
# - 2 vs 3: gana 3 (+1)
# - 4 vs 3+1: empate
# - 2 vs 4: gana 4 (+2)
# Resultado: "2b"

lista_a_2 = [4, 4, 4]
lista_b_2 = [2, 8, 2]

resultado = battle(lista_a, lista_b)  # -> "x"

# Explicación:
# - 4 vs 2: gana 4 (+2)
# - 4+2 vs 8: gana 8 (+2)
# - 4 vs 2+2: empate
# Resultado: "x"
"""

import os

os.system("cls")

lista_a = [2, 4, 2]
lista_b = [3, 3, 4]

lista_a_2 = [4, 4, 4]
lista_b_2 = [2, 8, 2]


def battle(lista_a: list[int], lista_b: list[int]) -> str:
    """
    Batalla de arreglos, recibe dos arreglos, velida la diferencia entre los numeros de cada arreglo y el numero final obtiene la diferencia entre los
    elementos de los arreglos

    Args:
        lista_a (list[int]): primera lista de batalla
        lista_b (list[int]): segunda lista de batalla

    Return:
        str, con la diferencia entre los ultimos elementos de cada arreglo y la letra del arreglo

    Ejemplo:
        # - 2 vs 3: gana 3 (+1)
        # - 4 vs 3+1: empate
        # - 2 vs 4: gana 4 (+2)
        # Resultado: "2b"
    """
    if len(lista_a) != len(lista_b):
        raise ValueError("las listas de batalla deben ser del mismo tamaño")

    dif_a = 0
    dif_b = 0

    for i in range(len(lista_a)):

        num_a = lista_a[i] + dif_a
        num_b = lista_b[i] + dif_b

        if num_a == num_b:
            dif_a = 0
            dif_b = 0
            continue

        if num_a > num_b:
            dif_a = num_a - num_b
            dif_b = 0
            continue

        if num_b > num_a:
            dif_b = num_b - num_a
            dif_a = 0
            continue

    if dif_a != 0:
        return f"{dif_a}a"

    if dif_b != 0:
        return f"{dif_b}b"

    return "x"


print(battle(lista_a=lista_a, lista_b=lista_b))
print(battle(lista_a=lista_a_2, lista_b=lista_b_2))


def battle_short(lista_a: list[int], lista_b: list[int]):
    """
    Batalla de arreglos, recibe dos arreglos, velida la diferencia entre los numeros de cada arreglo y el numero final obtiene la diferencia entre los
    elementos de los arreglos

    Args:
        lista_a (list[int]): primera lista de batalla
        lista_b (list[int]): segunda lista de batalla

    Return:
        str, con la diferencia entre los ultimos elementos de cada arreglo y la letra del arreglo

    Ejemplo:
        # - 2 vs 3: gana 3 (+1)
        # - 4 vs 3+1: empate
        # - 2 vs 4: gana 4 (+2)
        # Resultado: "2b"
    """
    points_a = sum(lista_a)
    points_b = sum(lista_b)

    if points_a > points_b:
        return f"{points_a-points_b}a"
    if points_b > points_a:
        return f"{points_b - points_a}b"
    return "x"


print(battle_short(lista_a=lista_a, lista_b=lista_b))
