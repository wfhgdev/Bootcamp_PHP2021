#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el
# número de veces que aparece la letra en la frase
contador = int(0)
txt = str(input("Digite frase: "))
letra = str(input("Digite letra a buscar: "))
for x in txt:
    if x == letra:
        contador += 1
print(f"La letra '{letra}' aparece en el texto {contador} veces")