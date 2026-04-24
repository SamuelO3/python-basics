"""
Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda.
Se utilizan para la búsqueda de cadenas de texto, validación de datos, etc.
"""

""" ¿Por qué aprender Regex?

- Búsqueda avanzada: Encontrar patrones específicos en textos grandes de forma rápida y precisa. (un editor de Markdown sólo usando Regex)

- Validación de datos: Asegurarte que los datos que ingresa un usuario como el email, teléfono, etc. son correctos.

- Manipulación del texto: Extraera, reemplazar y modificar partes de la cadena de texto fácilmente
"""

import os

os.system("cls")

# Importar el modulo de expresiones regulares
import re

# creamos un pattern, que es una cadena de texto que describe lo que queremos enecontrar
pattern = "mundo"
# el texto donde queremos buscar
text = "Hola mundo"
# usamos la funcion de busqueda re
result = re.search(pattern=pattern, string=text)

if result:
    print("Ha encontrado el pattern")
else:
    print("No ha encontrado el pattern")

#! Usar estas funciones o metodos en un try/except ya que dan errores si no tienen returns

# .group devuelve la cadena que coincide con el pattern.
text_chain = result.group()
print(text_chain)

# .start() devuelve la posicion inicial de la coincidencia (primer caracter del pattern)
coincidense_position = result.start()
print(coincidense_position)
# .end() devuelve la posicion final de la coincidencia (ultimo caracter del pattern)
coincidense_position = result.end()
print(coincidense_position)

print("Ejercicio ------------------------------------------------------------")
# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la coincidencia.
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
pattern = "IA"

result = re.search(pattern=pattern, string=text)
first_location = result.group()
first_char = result.start()
last_char = result.end()
print(
    f"Ocurrencia: {first_location} Primer caracter: {first_char} Ultimo caracter: {last_char}"
)

print("#* -------------------------------------------------------------------------")

# el metodo .findall() devuelve una lista con todas las coincidencias de la palabra pattern
text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Python"
print(
    f"Lista con todas las coincidencias del pattern: {re.findall(pattern=pattern, string=text)}"
)

print("#* -------------------------------------------------------------------------")

# .iter() Devuleve un iterable que contiene todos los resultados de la busqueda.
text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Python"
matches = re.finditer(pattern=pattern, string=text)

for m in matches:
    print(
        f"grupo: {m.group()}, primer caracter: {m.start()}, ultimo caracter: {m.end()}"
    )

print("Ejercicio ------------------------------------------------------------")

# EJERCICIO 02
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que posición empieza y termina cada coincidencia y cuantas veces se encontró.
text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"
pattern = "midu"
matches = re.finditer(pattern=pattern, string=text)
cantidad = 0
for m in matches:
    print(
        f"grupo: {m.group()}, primer caracter: {m.start()}, ultimo caracter: {m.end()}"
    )
    cantidad += 1
print(f"El pattern se encontro {cantidad} veces")

print("#* -------------------------------------------------------------------------")

###! Modificadores

# Los modificadores son opciones que se pueden agregar a un pattern para cambiar su comportamiento

# re.IGNORECASE: ignora las mayuscualas y las minusculas


text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala. ¡Viva la Ia!"
pattern = "ia"

found = re.findall(pattern=pattern, string=text, flags=re.IGNORECASE)
if found:
    print(found)

print("Ejercicio ------------------------------------------------------------")

# EJERCICIO 03
# Encuentra todas las ocurrencias de la palabra "python" en el siguiente texto, sin distinguir entre mayúsculas y minúsculas.
text = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"
pattern = "python"
result = re.findall(pattern, text, re.IGNORECASE)
if result:
    print(result)

print("#* -------------------------------------------------------------------------")

###! Reemplazar el texto

# .sub() reemplaza todas las coincidencias de un patrón en un texto

text = "Hola, mundo! Hola de nuevo. Hola otra vez."
pattern = "hola"
replacement = "Adiós"
print(text)

new_text = re.sub(pattern=pattern, repl=replacement, string=text, flags=re.IGNORECASE)
print(new_text)