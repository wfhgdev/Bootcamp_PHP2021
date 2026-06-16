import json
estudiante = {"codigo":123, "nombre":"Jose", "nota":4}
"""formatoJson = json.dumps(estudiante)
print(formatoJson)
estudiante1 = json.loads(formatoJson)
print(estudiante1)"""
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
general = {"estudiantes":lista}
archivo = open("estudiante1.json","w")
respuesta = json.dump(general,archivo,indent=3)
archivo.close()