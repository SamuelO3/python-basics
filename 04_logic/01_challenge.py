"""
¿Está en Equilibrio la Alianza entre Reed Richards y Johnny Storm?

En el universo de los 4 Fantásticos, la unión y el equilibrio entre los poderes es fundamental para enfrentar cualquier desafío.
En este problema, nos centraremos en dos de sus miembros:

Reed Richards (Mr. Fantastic), representado por la letra R.
Johnny Storm (La Antorcha Humana), representado por la letra J.

Objetivo:

Crea una función en Python que reciba una cadena de texto.
Esta función debe contar cuántas veces aparece la letra R (para Reed Richards) y cuántas veces aparece la letra J (para Johnny Storm) en la cadena.

- Si la cantidad de R y la cantidad de J son iguales, se considera que la alianza entre la mente y el fuego está en equilibrio y la función debe retornar True.
- Si las cantidades no son iguales, la función debe retornar False.
- En el caso de que no aparezca ninguna de las dos letras en la cadena, se entiende que el equilibrio se mantiene (0 = 0), por lo que la función debe retornar True.
"""

import os

os.system("cls")

sentence = "RRRRJJJjjjjrrr"


def words_counter(sentence: str):
    """
    Esta funcion verifica cuantas (R,r) y (J,j) aparecen en un texto

    Args:
        sentence (str): texto a validar

    Return:
        True si la cantidad de ambas es igual, False si no
    """
    r_count = 0
    j_count = 0

    for w in sentence:
        if w.upper() == "R":
            r_count += 1
            continue
        if w.upper() == "J":
            j_count += 1

    return r_count == j_count


print(words_counter(sentence))
print(words_counter("RrJj"))
print(words_counter("RRrJ"))
print(words_counter("RrJJJ"))
print(words_counter("ABSCD"))


haystack = "otomatetomas"
needle = "tomas"


def strStr(haystack: str, needle: str):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    count = haystack.count(f"{needle}")
    if count > 0:
        index = haystack.index(f"{needle}")
        return count, index
    return False


print(strStr(haystack=haystack, needle=needle))
