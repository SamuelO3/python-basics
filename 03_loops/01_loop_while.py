import os

os.system("cls")

###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")
contador = 0
while contador <= 10:
    contador += 1
    print(contador)

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")
contador = 0
suma = 0
while contador <= 20:
    contador += 1
    if contador % 2 == 0:
        suma += contador
print(suma)


# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")
numero = 0
factorial = 1
while True:
    try:
        numero = int(input("introduce un numero positivo: "))
        if numero <= 0:
            print("numero no valido")
            continue
    except:
        print("numero no valido")

    while numero > 0:
        factorial *= numero
        numero -= 1
    break

print(factorial)

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
# print("\nEjercicio 4:")

# password = "Tomas"
# while True:
#     passw = input("introduce tu contraseña (sin espacios y minimo 8 caracteres):  ")
#     if len(passw) < 8 or " " in passw:
#         print("contraseña no valida")
#         continue

#     if passw == password:
#         print("Contraseña correcta")
#         break


# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

while True:
    try:
        numero = int(input("introduce un numero positivo: "))
        if numero <= 0:
            print("numero no valido")
            continue
    except:
        print("numero no valido")

    contador = 1
    while contador <= 10:
        print(f"{contador} * {numero}: ", contador * numero)
        contador += 1
    break
# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

n = int(input("Introduce un número entero positivo N: "))

numero = 2
while numero <= n:
    es_primo = True
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            es_primo = False
            break
        divisor += 1
    if es_primo:
        print(numero)

    numero += 1
