# Recibir el número del día y mostrar su nombre
dias = ("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")
while (True):
    try:
        numero = int(input("Escriba el numero del dia: "))
        if (numero >= 1 and numero <= 7):
            print(numero, dias[numero-1])
            break
        else:
            print("Numero fuera del rango de los dias [1-7]")
    except ValueError as mensaje:
        print("Solo numeros por favor")