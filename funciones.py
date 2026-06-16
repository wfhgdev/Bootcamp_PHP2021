def saludo():
    print("Saludo para todos")
####################################################
def sumar(sumando1,sumando2):
    suma = sumando1 + sumando2
    print(f"El resultado de la suma es: {suma}")
####################################################
def multiplicar(sumando1, sumando2):
    multiplicacion = sumando1 * sumando2
    print(f"El resultado de la multiplicación es: {multiplicacion}")
####################################################
def restar(sumando1, sumando2):
    resultado = sumando1 - sumando2
    print(f"El resultado de la resta es: {resultado}")
###################################
def pintarDatos(nombre="", apellido=""):
    if(nombre=="" or apellido == ""):
        print("Debe enviar los dos parametros nombre y apellido")
    else:
        print(f"El nombre es {nombre}")
        print(f"El apellido es {apellido}")
#######################################
def main():
    otro = int(input("Escriba el primer número: "))
    otroMas = int(input("Escriba el segundo número: "))
    sumar(otro,otroMas)
    multiplicar(otro,otroMas)
    restar(otroMas, otro)

pintarDatos()

