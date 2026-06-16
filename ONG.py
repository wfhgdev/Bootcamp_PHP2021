Existencias = 1000
print("El saldo actual de vacunas es: " + str(Existencias))
while Existencias >= 200:
    Consumo = int(input("Digite cantida de vacunas a consumir: "))
    if Consumo < Existencias:
        Existencias = Existencias - Consumo
        print("El saldo actual de vacunas es: " + str(Existencias))
    else:
        print("La cantidad solicitada es mayor a existencias actuales que son iguales a: " + str(Existencias))
print("Se llego al limite minimo de vacunas, el saldo de vacunas actual es: " + str(Existencias))