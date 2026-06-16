#Codigo que pida 2 números de 4 dígitos y diga cual o cuales de ellos es par o es impar
num1 = num2 = int(0)
prueba= "falso"
while prueba == "falso":
    num1 = int(input("Digite primer numero de cuatro digitos: "))
    if num1 >= 1000 and num1 <= 9999:
        prueba = "verdadero"
    else:
        print("El numero digitado no es de cuatro digitos")
prueba= "falso"
while prueba == "falso":
    num2 = int(input("Digite segundo numero de cuatro digitos: "))
    if num2 >= 1000 and num2 <= 9999:
        prueba = "verdadero"
    else:
        print("El numero digitado no es de cuatro digitos")
if (num1 % 2) == 0:
    print(f"El primer numero: {num1} es par")
else:
    print(f"El primer numero: {num1} es impar")
if (num2 % 2) == 0:
    print(f"El segundo numero: {num2} es par")
else:
    print(f"El segundo numero: {num2} es impar")