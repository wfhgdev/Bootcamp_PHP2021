import os
# 100 – 200	Asistente
# 200 - 300	Coordinador
# Un programa que apartir de la tabla de rango salarial, 
# se reciban la funciones, luego permitir leer nombre y salario
# el programa debe solicitar a los asistentes un color favorito
# al final se debe mostar los empleados con su color favorito y sus funciones
# a los no asistentes asignar el color blue
def mostrar(listaEmpleados):
    os.system("cls")
    print("************ Respuesta al Subreto ####################")
    for empleado in listaEmpleados:
        salida = empleado["nombre"]+" -- "+str(empleado["salario"])+" -- "+empleado["cargo"]+" -- "+empleado["color"]
        print(salida)
def cargarColor(listaEmpleados):
    for empleado in listaEmpleados:
        if(empleado["cargo"]=="Asistente"):
            texto = "Digame el color favorito: " + empleado["nombre"]+" : "
            color = input(texto)
            empleado["color"] = color
        else:
            empleado["color"]="blue"
def llenarLista(rangoSalarial1,rangoSalarial2):
    listaEmpleados = []
    while (True):
        os.system("cls")
        print("********** LLenado de lista de empleados ************")
        nombre = input("Nombre: ")
        salario = float(input("Salario: "))
        empleado = {"nombre":nombre,"salario":salario}

        if(salario>=rangoSalarial1["inferior"] and salario<rangoSalarial1["superior"]):
            empleado["cargo"] = rangoSalarial1["cargo"]
        else:
            empleado["cargo"] = rangoSalarial2["cargo"]

        listaEmpleados.append(empleado)
        respuesta = input("¿Desea continuar SI/NO?")
        respuesta = respuesta.upper()
        if(respuesta=="NO"):
            break
    return listaEmpleados

def main():
    rangoSalarial1 = {"inferior":100,"superior":200,"cargo":"Asistente"}
    rangoSalarial2 = {"inferior":200,"superior":300,"cargo":"Coordinador"}
    texto = "Escriba las funciones para " + rangoSalarial1["cargo"] + " :"
    funciones = input(texto)
    rangoSalarial1["funciones"] = funciones
    funciones = input("Escriba las funciones para Coordinador: ")
    rangoSalarial2["funciones"] = funciones
    listaEmpleados = llenarLista(rangoSalarial1,rangoSalarial2)
    cargarColor(listaEmpleados)
    mostrar(listaEmpleados)

main()