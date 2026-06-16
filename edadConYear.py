#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha
#cumplido (desde 1 hasta su edad)
import datetime
Year = (datetime.datetime.now()).year
edad = int(input("Digite edad: "))
cuenta = Year - edad
for x in range(edad):
    print(f"En el año {cuenta} tenia {x+1} años de edad")
    cuenta += 1