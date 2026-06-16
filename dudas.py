import os
def mostrar(valor,otro,unomas,dosmas,cuatromas):
    print("Esto es el mensaje: ",valor)

def sumar(a,b):
    return a+b

def main():
    sumando1 = 45
    sumando2 =54
    suma = sumar(sumando1,sumando2)
    suma = suma * 3
    print(suma)

def ejemploOpcion():
    while (True):
        opcion = ""
        os.system("cls")
        nombre = input("Nombre:")
        edad = input("Edad: ")
        while(opcion!="SI" and opcion!="NO"):
            opcion = input("Desea continuar SI/NO: ")
        
        if(opcion=="NO"):
            break