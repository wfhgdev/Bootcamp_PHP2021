import os
#Metodo que me permite recibir dos numeros y retornar la suma resultado
def sumar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado
def multiplicar(numero1, numero2):
    resultado = 0
    for numero in range(numero2):
        resultado = sumar(resultado,numero1)
    return resultado
"""
Escriba un programa que permita crear una lista de palabras. 
Para ello, el programa tiene que pedir un número y luego 
solicitar ese número de palabras para crear la lista. 
Por último, el programa tiene que mostrar los elementos 
de la lista en mayúsculas y minúsculas de la siguiente forma
"""
def uno():
    numero = int(input("Escriba la cantidad de palabras: "))
    lista = []
    for item in range(numero):
        palabra = input(f"Escriba una palabra {item}: ")
        lista.append(palabra)
    contador = 1
    for palabra in lista:
        palabraMay = palabra.upper()
        palabraMin = palabra.lower()
        print(f"{contador}  -  {palabraMay}  -  {palabraMin}")
        contador = contador + 1
"""
Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. 
Copia los elementos de la lista en otra lista, pero en orden inverso, 
y muestra los elementos de la nueva lista por la pantalla.
"""
def dos():
    lista = []
    for i in range(5):
        cadena = input("Escriba una cadena: ")
        lista.append(cadena)
    lista1 = []
    cantidad = len(lista)
    for i in range(cantidad-1,-1,-1):
        lista1.append(lista[i])
    print(cantidad)
    print(lista1)

################# La función MENÚ
def menu():
    while (True):
        os.system("cls")
        print("1. Para el primer ejercicio")
        print("2. Para el segundo ejercicio")
        print("3. Para salir")
        opcion = input("Ingrese una opción: ")
        if(opcion=="1"):
            uno()
        elif(opcion == "2"):
            dos()
            input()
        elif(opcion=="3"):
            print("Gracias por usar el programa")
            break
        else:
            print("Opción fuera del rango")

def main():
   menu()
main()