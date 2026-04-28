import os

os.system("cls")

import re

"""
Los cuantificadores se utilizan para especificar cuantas ocurrencias de un caracter o grupo de caracteres
se deben encontrar en una cadena
"""

print("#* -------------------------------------------------------------------------")
# * significa que puede aparecer cero o mas veces
text = "aaaba"
pattern = r"a*"  # Especifica que la a pueda aparecer cero o mas veces

matches = re.findall(pattern, text)
if matches:
    print(matches)


print("#* -------------------------------------------------------------------------")
# +: Una a más veces
text = "dddd aaa ccc a bb aa casa"
pattern = r"a*b"
matches = re.findall(pattern, text)
if matches:
    print(matches)

print("#* -------------------------------------------------------------------------")
# ? cero o una vez
text = "aaabacb"
pattern = r"a?b"
matches = re.findall(pattern, text)
if matches:
    print(matches)

print("Ejercicio ------------------------------------------------------------")
# Ejercicio: Haz opcional que aparezca un +34 en el siguiente texto
phone = "+57 688999999"
pattern = r"(\+|00)?\d{1,3} ?\d{9}"
valid = re.search(pattern, phone)
if valid:
    print("Numero con prefijo")
else:
    print("numerno sin prefijo")
print("#* -------------------------------------------------------------------------")

# {n} exactamente n veces
text = "aaaaaa         aa   aaaa"
pattern = r"a{3}"
matches = re.findall(pattern, text)
if matches:
    print(matches)

# {n, m}: De n a m veces
text = "u uu uuu u"
pattern = r"\w{2,3}"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio:
# Encuentra las palabras de 4 a 6 letras en el siguiente texto
words = "ala casa árbol león cinco murcielago"
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern, words)
if matches: print(matches)
