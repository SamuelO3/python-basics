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


def counter_r_j(sentence: str) -> bool:
    """
    La funcion valida estabilidad de la alianza de Mr. Fantastic y La Antorcha Humana
    Args:
        sentence (str): cadena de texto a validar
    Returns:
        bool: 
            True si la alianza esta estable (numero de letras de ambos iguales)\n
            False (bool): si la alianza es inestable (numero de letras desigual)
    """
    count_r = 0
    count_j = 0
    for l in sentence:
        if l.lower() == "r":
            count_r += 1
        elif l.lower() == "j":
            count_j += 1

    # if count_j == count_r:
    #     return True
    # elif (count_r > count_j) or (count_r < count_j):
    #     return False
    
    # if (count_r == 0) and (count_j == 0):
    #     return True
    return count_j == count_r
    

if counter_r_j(sentence) is True:
    print("La alianza es estable")
else:
    print("La alianza es inestable")
