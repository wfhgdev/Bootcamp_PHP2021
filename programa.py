import os
print("Programa que te dice si eres mayor de edad o no")
contador = 0
while (contador < 5):
	contador += 1
	edad = int(input("Escribe la edad: "))
	if (edad >= 18):
		print("Eres mayor de edad")
	else:
		print("Aun te falta para entrar a ciertos lugares")
	opcion = input("No, para no Limpiar pantalla").upper()
	if(opcion!="NO"):
		os.system("cls")