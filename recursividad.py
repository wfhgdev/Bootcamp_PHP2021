def conteo(numero):
    numero = numero -1
    if(numero > 0):
        print(numero)
        conteo(numero)
    else:
        print("Corramos.....")

def factorial(numero):
    resultado = 1
    for i in range(1,numero+1):
        resultado = resultado * i
    return resultado

def factorialR(numero):
    if(numero>1):
        return numero * factorialR(numero-1)
    else:
        return 1

re = factorialR(7)
print(re)
