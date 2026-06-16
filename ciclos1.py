# Lea nombres hasta que escriban salir y agregar a una lista
def lectura():
    lista = []
    while (True):
        nombre = input("Escriba el dato: ")
        lista.append(nombre)
        if(nombre == "salir"):
            break
    print(lista)
lectura()