x= i = j = 0
lista = []
tamano = int(input("Digite tamaño de lista de numeros: "))
while x <= (tamano-1):
    lista.append(int(input("Digite un numero para agregar a la lista : ")))
    x += 1
print(f"Lista sin ordenar: {lista}")
for i in range(x):
    for j in range(0, x-1):
        if (lista[j]) > (lista[j+1]):
            aux = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = aux
print(f"Lista ordenada de menor a mayor: {lista}")