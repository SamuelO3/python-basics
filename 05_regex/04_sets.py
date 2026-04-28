


import os
os.system("cls")

import re

print("#* -------------------------------------------------------------------------")
# [] coincide con cualquier caracter dentro de los corchetes
username = "el_r$ub.ius_69+"
pattern = r"^[\w._%+-]+$"

match = re.search(pattern, username)
if match: print("Usuario valido")
else: print("Usuario no valido")

# Buscar todas las vocales de una palabra
text = "Hola mundo"
pattern = r"[aeiou]"
matches = re.findall(pattern, text)
print(matches)
print("#* -------------------------------------------------------------------------")

# Una Regex para encontrar las palabras man, fan y ban
# pero ignora el resto
text = "man ran fan ñan ban"
pattern = r"[mfb]an"
matches = re.findall(pattern, text)
print(matches)

print("Ejercicio ------------------------------------------------------------")
# Ejercicio:
# Nos han complicado el asunto, porque ahora hay palabras que encajan pero no empiezan por esas letras.
# Solo queremos las palabras man, fan y ban
text = "omniman fanatico man bandana"
pattern = r"\b[mfb]an\b"
matches = re.findall(pattern, text)
print(matches)

print("#* -------------------------------------------------------------------------")
text = "22"
pattern = r"[4-9]"

matches = re.findall(pattern, text)
print(matches)

pattern = r"[a-z]"  #Rango de la a a la z
pattern = r"[a-zA-Z]" #Rango de la a a la z minusculas y maysuculas
pattern = r"[a-zA-Z0-9]" #Rango de la a a la z minusculas y maysuculas y numeros del 0 al 9

print("#* -------------------------------------------------------------------------")
# [^]: Coincide con cualquier caracter que no esté dentro de los corchetes
text = "Hola mundo"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print(matches)

print("Ejercicio ------------------------------------------------------------")
# Ejercicio final con todo lo aprendido
# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png

## Buscar corner cases que no pasa y arreglarlo:
# no pasan
"michael@gov.co.uk"
"lo.que+sea@shopping.online"
'"Jane.Doe."@example.com'
email = '"Jane..Doe"@example.com'
pattern = r'[\w\.\_\%\+\-\"]+@[\w\.\-]+\.[a-zA-Z]{2,4}'

valid = re.search(pattern, email)
if valid: 
    print("Correo valido")
else:
    print("Correo no valido")


