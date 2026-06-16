#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los
#números impares desde 1 hasta ese número separados por comas
lista = []
num = int(input("Digite número entero y positivo: "))
if num >= 1:
    for x in range(1,num+1):
        if (x % 2) != 0:
            lista.append(x)
print(lista)