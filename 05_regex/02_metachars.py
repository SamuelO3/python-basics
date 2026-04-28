import os

os.system("cls")


import re

"""
Los metacaracteres son simbolos especiales con significados especificos en las expresiones regulares.
"""

# El punto (.)
# coincidir con cualquier caracter excepto una nueva linea
text = "Hola mundo, H0la denuevo, H$la otra vez"
pattern = "H.la"  # Encontrara cualquier caracter sin importar cual sea

found = re.findall(pattern, text)
if found:
    print(found)

text = "casa caasa cosa cisa cesa causa"
pattern = "c.sa"

matches = re.findall(pattern, text)
print(matches)

print("#* -------------------------------------------------------------------------")

text = "Hola mundo, H0la denuevo, H$la otra vez"
pattern = r"H.la"  # la r indica que se esta creando una expresion regular

found = re.findall(pattern, text)
if found:
    print(found)

print("#* -------------------------------------------------------------------------")

text = "Mi casa es blanca. Y mi coche es negro."
pattern = r"\."  # el \ indica que se ignore el significado especial del metacaracter, por lo tanto ahora buscará los puntos en el texto
found = re.findall(pattern, text)
if found:
    print(found)

print("#* -------------------------------------------------------------------------")
# \d: coincide con cualquier digito que sea del 0 al 9

text = "El numero del telefono es: 3215647885"
pattern = r"\d{9}"  # el \d indica que se busque cualquier digito del 0 al 9 y el {9} indica la cantidad de numeros que debe tener la coincidencia (por defecto es uno)
found = re.findall(pattern, text)
if found:
    print(found)

print("Ejercicio ------------------------------------------------------------")
# Ejercicio: Detectar si hay un número de España en el texto gracias al prefijo +34
text = "Mi número de teléfono es +34 688999999 apúntalo vale?"
pattern = r"\+34 \d{9}"
found = re.findall(pattern, text)
if found:
    print(found)

print("#* -------------------------------------------------------------------------")

# \w coincide cualquier caracter alfanumerico (a-z, A-Z, 0-9, _)
text = "@@&%El_rubis_69"
pattern = r"\w"
found = re.findall(pattern, text)
if found:
    print(found)

print("#* -------------------------------------------------------------------------")

# \s coincide con cualquier espacio en blanco (espacio, tabulacion, salto de linea)
text = "Hola mundo\n¿como estas?\t"
pattern = r"\s"
found = re.findall(pattern, text)
if found:
    print(found)

print("#* -------------------------------------------------------------------------")
# ^ coincide con el principio de una cadena
text = "%123_mi_nombre"
pattern = r"^\w"  # validar nombre de usuario

valid = re.search(pattern, text)

if valid:
    print("Nombre de usuario valido")
else:
    print("Nombre de usuario no valido")

my_phone = "+57 320659845"
pattern = r"^\+\d{1,3} \d{9}"

valid = re.search(pattern, my_phone)
if valid:
    print("Numero de telefono valido")
else:
    print("Numero de telefono no valido")

print("#* -------------------------------------------------------------------------")
# $ coincide con el final de una cadena

text = "Hola mundo"
pattern = r"mundo$"
valid = re.search(pattern, text)

if valid:
    print("Cadena de texto valida")
else:
    print("Cadena de texto no valida")

print("Ejercicio ------------------------------------------------------------")

# EJERCICIO
# Valida que un correo sea de gmail
text = "miduga@gmail.com"
pattern = r"@gmail.com$"
valid = re.search(pattern, text)

if valid:
    print("Correo valido")
else:
    print("Correo no valido")

print("Ejercicio ------------------------------------------------------------")
# EJERCICIO:
# Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extension .txt
files = "file1.txt file2.pdf midu-of.webp secret.txt"
pattern = r"\w+\.txt" #Busca cualquier palabra alfanumerica que contenga .txt en ella  
found = re.findall(pattern, files)

if found: print(found)

print("#* -------------------------------------------------------------------------")

# \b coincide con el final o principio de una palabra
text = "casa casada cosa cosas casado casa"
pattern = r"\bcasa\b"

found = re.findall(pattern, text)
if found: print(found)

print("#* -------------------------------------------------------------------------")
# | coincide con cualquiera de las dos opciones.

fruits = "platano, piña, manzana, aguacate, palta, pera, aguacate, aguacate"
pattern = r"palta|aguacate"

found = re.findall(pattern, fruits)
if found: print(found)