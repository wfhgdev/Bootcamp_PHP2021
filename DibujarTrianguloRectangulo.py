#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo
#como el de más abajo, de altura el número introducido
x = int(1)
num = int(input("Digite numero entero: "))
acumulador = str("*")
if num > 0:
    for x in range(num):
        print(acumulador)
        acumulador += "*"