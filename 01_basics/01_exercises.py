###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
system("cls")

# print("\nEjercicio 1: Imprimir mensajes")
# print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

# name = input("Escribe tu nombre: ")
# city = input("Escribe tu ciudad: ")

# print(f"Mi nombre es {name}, vivo en {age} colombia")

# print("--------------")

# print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
# print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
# a = 15
# b = 3.14159
# c = "Hola mundo"
# d = True
# e = None

# print(f"Esta variable de tipo: {type(a)}")
# print(f"Esta variable de tipo: {type(b)}")
# print(f"Esta variable de tipo: {type(c)}")
# print(f"Esta variable de tipo: {type(d)}")
# print(f"Esta variable de tipo: {type(e)}")

# ### Completa aquí

# print("--------------")

# print("\nEjercicio 3: Casting de tipos")
# print("Convierte la cadena \"12345\" a un entero y luego a un float.")
# print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

# cadena = "12345"
# entero = int(cadena)
# print(entero)
# decimal = float(entero)
# print(decimal)

# decimal2 = 3.99
# entero2 = int(decimal2)
# print(entero2)

# ### Completa aquí

# print("--------------")

# print("\nEjercicio 4: Variables")
# print("Crea variables para tu nombre, edad y altura.")
# print("Usa f-strings para imprimir una presentación.")

# stature = input("ingresa tu estatura en centimetros:")
# age = input("Escribe tu edad: ")

# print(f"Hola me llamo {name}, tengo {age} años y mido {stature} centimetros")

# ### Completa aquí

# print("--------------")

# print("\nEjercicio 5: Números")
# print("1. Crea una variable con el número PI (sin asignar una variable)")
# print("2. Redondea el número con round()")
# print("3. Haz la división entera entre el número que te salió y el número 2")
# print("4. El resultado debería ser 1")

pi = int(round(3.1416)/2)
print(f"pi redondeado: {round(3.1416)}")
print(f"pi redondeado y dividido entre 2: {round(3.1416)/2}")
print(f"pi redondeado y dividido entre 2, convertido en entero: {pi}")
