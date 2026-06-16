import os
"""
Programa para recibir un listado de textos con los siguientes
datos: codigo, titulo, cantidad, costo, precio
Mostrar el subtotal invertido por cada libro y el total invertido.
Preguntar al usuario si desea registrar otro Libro
"""
def comprar():
    listaLibros = []
    while (True):
        codigo = input("Escriba el código: ")
        titulo = input("Escriba el titulo: ")
        while(True):
            try:
                cantidad = int(input("Escriba la cantidad: "))
                if(cantidad>0):
                    while(True):
                        try:
                            costo = float(input("Escriba el costo: "))
                            while(True):
                                try:
                                    precio = float(input("Escriba el precio: "))
                                    libro = {"codigo":codigo,"titulo":titulo,"cantidad":cantidad,"costo":costo,"precio":precio}
                                    listaLibros.append(libro)
                                    break
                                except:
                                    print("Sr. Usuario el precio debe ser numerico")
                            break
                        except:
                            print("Sr. Usuario el costo debe ser numerico")
                    break
                else:
                    print("La cantidad debe ser mayor a cero")
            except:
                print("Sr. Usuario La cantidad debe ser numerica")
        opcion = input("Si no desea agregar mas libros escriba NO: ").upper()
        if(opcion=="NO"):
            break
    os.system("cls")
    total = 0
    for libro in listaLibros:
        subTotal = libro["cantidad"] * libro["costo"]
        total = total + subTotal
        print(libro["titulo"],subTotal)
    print(f"El total invertido es: {total}")
"""
Programa para leer una lista de estudiantes hasta que no se quiera ingresar uno nuevo
con los siguientes datos: identidad, nombre, nota1, nota2, nota3
Mostrar el listado de estudiantes que gana la nota promedio (gana si el promedio es >= a 3)
Tome nota entre 0 y 5 y el promedio es ponderado, tambien el promedio del curso
"""

comprar()