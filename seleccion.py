def seleccion():
    lista = [2,3,5,8,4,1]
    cantidad = len(lista)
    for i in range(cantidad):
        for j in range(i+1,cantidad):
            if(lista[i]>lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    print(lista)

seleccion()