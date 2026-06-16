archivo = open("datos.txt","r")
datos = archivo.readlines()
archivo.close()

for elemento in datos:
    elemento = elemento.replace("\n","")
    print(elemento)