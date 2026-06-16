import json
archivo = open("estudiante1.json","r")
contenido = json.load(archivo)
archivo.close()
lis = contenido["estudiantes"]
for e in lis:
    print(e["nota"])
print(contenido)