edad = int(input("Digite la edad de la persona: "))
ocupacion = input("Digite ocupacion de la persona (empleado/contratista/pensionado/desempleado): ")
ocupacion= ocupacion.lower()
cantPersonas = int(input("Digite cantidad personas que conviven: "))
if edad > 80 and ocupacion == "empleado" and cantPersonas >= 12:
    print("Puede vacunarse enseguida")
if edad <= 80 and edad > 65 and ocupacion == "contratista" and cantPersonas >= 3 and cantPersonas <= 7:
    print("La vacunacion se agendara para julio")
if edad <= 65 and edad > 40 and ocupacion == "pensionado" and cantPersonas >= 8 and cantPersonas <= 11:
    print("La vacunacion se agendara para septiembre")
if edad <= 40 and edad >= 1 and ocupacion == "desempleado" and cantPersonas == 1 or cantPersonas == 2:
    print("La vacunacion se agendara para diciembre")