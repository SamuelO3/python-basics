import os
os.system("cls")





nombre = 'ana'
edad = 22
salario = 22500 
print(f"Hola soy {nombre}, tengo {edad} y gano {salario}")

def salary_level (salary: int) -> str:
    if salary >= 4500:
        return 'alto'
    elif salary >= 3000:
        return 'medio'
    else:
        return 'bajo'
    
print(salary_level(3500))

salarios = [5200, 3800, 3600, 3900, 4100, 2900, 3400, 3100, 2800, 3500]

for salary in salarios:
    if salary > 3500:
        print(f'Mayor que 3500 {salary}')

new_list = [s for s in salarios if s > 3500]
print(new_list)

empleados = {
    "Ana": 5200,
    "Carlos": 3800,
    "María": 3400,
    "Diego": 3900
}
for nombre, salario in empleados.items():
    print(f"hola soy {nombre} y gano {salario}" )

salario_mayor = 0
nombre_mayor = ""
for nombre, salario in empleados.items():
    if salario > salario_mayor:
        salario_mayor = salario
        nombre_mayor = nombre
print(f"hola soy {nombre_mayor} y gano {salario_mayor}" )

def calcular_aumento(salario_actual: float, porcentaje: float) ->float:
    return (salario_actual * porcentaje) + salario_actual
print(calcular_aumento(3500, 0.1))

empleados = [
    {"nombre": "Laura",   "salario": 5200, "departamento": "Ingeniería"},
    {"nombre": "Carlos",  "salario": 3800, "departamento": "Ingeniería"},
    {"nombre": "Sofía",   "salario": 4100, "departamento": "Marketing"},
    {"nombre": "María",   "salario": 3400, "departamento": "Diseño"},
]

def departamento_indicado(empleados_lista:list, departamento:str):
    for dic in empleados_lista:
        if dic['departamento'] == departamento:
            print(f"empleado {dic['nombre']} del departamento de {dic['departamento']} gana {dic['salario']}")

departamento_indicado(empleados, 'Ingeniería')


nombres = [" ana ", "CARLOS", " maría ", "DIEGO "]

nueva_lista = [n.strip().lower() for n in nombres]
print(nueva_lista)

datos = "ingeniería, marketing, diseño, recursos humanos"
nuevos_datos = [d.strip(' ') for d in datos.split(",")]
datos = " | ".join(nuevos_datos)
print(datos)

proyectos = ["App Mobile", "Rediseño web", "Campaña Q2", "API Pagos"]
[print(f"{i+1}. {p}") for i,p in enumerate(proyectos)]

empleados = [
    {"nombre": "Laura", "salario": 5200}, 
    {"nombre": "Carlos", "salario": 3800}, 
    {"nombre": "Sofía", "salario": 4100}, 
    {"nombre": "Diego", "salario": 3900}
]

ordenados = sorted(empleados, key=lambda e:e['salario'], reverse=True)

for e in ordenados:
    print(f"{e['nombre']}: ${e['salario']}")


verificados = {}