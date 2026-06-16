diccionario1 = {"nombre":"Carlos","nota":3,"comentario":"Hola"}
diccionario2 = {"nombre":"Juan","nota":4,"comentario":"Hola1"}
diccionario3 = {"nombre":"Ana","nota":2,"comentario":"Hola2"}
diccionario4 = {"nombre":"Ana1","nota":2,"comentario":"Hola2"}
diccionario5 = {"nombre":"Ana2","nota":5,"comentario":"Hola2"}
diccionario6 = {"nombre":"Ana3","nota":4,"comentario":"Hola2"}
diccionario7 = {"nombre":"Ana4","nota":1,"comentario":"Hola2"}
lista = [diccionario1]
lista.append(diccionario2)
lista.append(diccionario3)
lista.append(diccionario4)
lista.append(diccionario5)
lista.append(diccionario6)
lista.append(diccionario7)
n = len(lista)
for i in range(n):
    for j in range(i+1,n):
        if(lista[i]["nota"]<lista[j]["nota"]):
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
print(lista[0])
print(lista[n-1])
acumulada= 0
for e in lista:
    acumulada = acumulada + e["nota"]
print(acumulada)
promedio = acumulada / n
print(promedio)