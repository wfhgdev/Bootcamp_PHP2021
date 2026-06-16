# Lea 5 nombres y agregar a una lista
def sinCiclos():
    lista = []
    nombre = input("Escriba el nombre: ")
    lista.append(nombre)
    nombre = input("Escriba el nombre: ")
    lista.append(nombre)
    nombre = input("Escriba el nombre: ")
    lista.append(nombre)
    nombre = input("Escriba el nombre: ")
    lista.append(nombre)
    nombre = input("Escriba el nombre: ")
    lista.append(nombre)
    print(lista)

def conFor():
    lista = []
    for iteracion in range(5):
        nombre = input("Escriba el nombre: ")
        lista.append(nombre)
    print(lista)

def conWhile():
    contador = 0
    lista = []
    while (contador<5):
        nombre = input("Escriba el nombre: ")
        lista.append(nombre)
        contador = contador + 1
    print(lista)
    for nombre in lista:
        print(nombre)

conWhile()