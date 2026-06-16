def ascendente(l):
    n = len(l)
    for i in range(n):
        for j in range(n-1):
            if(l[j] > l[j+1]):
                aux = l[j]
                l[j] = l[j+1]
                l[j+1] = aux
    print(l)
###############Descendente
def descendente(l):
    n = len(l)
    for i in range(n):
        for j in range(n-1):
            if(l[j] < l[j+1]):
                aux = l[j]
                l[j] = l[j+1]
                l[j+1] = aux
    print(l)

def ordenar(l,tipo):
    n = len(l)
    for i in range(n):
        for j in range(n-1):
            if(l[j] < l[j+1] and tipo =="desc"):
                aux = l[j]
                l[j] = l[j+1]
                l[j+1] = aux
            if(l[j] > l[j+1] and tipo =="asc"):
                aux = l[j]
                l[j] = l[j+1]
                l[j+1] = aux
    print(l)
def main():
    lista = []
    while (True):
        palabra = input("Escriba la palabra: ").lower()
        if(palabra == "salir"):
            break
        lista.append(palabra)
        
    ordenar(lista,"asc")

def longitud(lista):
    contador = 0
    for elemento in lista:
        contador +=1
    return contador
