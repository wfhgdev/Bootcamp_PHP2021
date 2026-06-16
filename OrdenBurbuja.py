vector = [250,190,1300,1,2,6,59,1024,650,800]
n=len(vector)
print("Vector desordenado: ")
print(vector)
for i in range(n):
    for j in range(0, n-1):
        if vector[j] < vector[j+1]:
            aux = vector[j]
            vector[j] = vector[j+1]
            vector[j+1] = aux
print("Vector ordenado por metodo Burbuja: ")
print(vector)