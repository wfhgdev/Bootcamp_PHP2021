#Un obrero necesita calcular su salario semanal, el cual se obtiene de la sig manera.
# Si trabaja 40 horas o menos se le paga 8000 por hora.
# Si trabaja más de 40 horas se le paga 8000 por cada una de las primeras 40 horas y 4500 por cada hora extra
salario = int(0)
horasTrabajadas = int(input("Digite horas trabajadas: "))
if horasTrabajadas <= 40:
    salario = horasTrabajadas * 8000
elif horasTrabajadas >40:
    salario = (40*8000)+((horasTrabajadas-40)*4500)
print(f"El salario total es: {salario}")