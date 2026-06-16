lista = ["Pedro","Ana","Karen"]
archivo = open("datos.txt","a")
for nombre in lista:
    nombre = nombre+"\n"
    archivo.write(nombre)
archivo.close()