from package_arrays.array_generales import *

bandera = True
lista = crear_lista(None, 10)
while bandera:
    opcion = get_int("1. Ingresar 10 numeros entre -1000 y 1000\n2. Salir\nIngrese una opcion: ", "Ingrese una de las opciones arriba mencionadas", 1, 2)
    match opcion:
        case 1:
            lista = get_list("Ingrese un numero(entre -1000 y 1000): ", "Reingrese el numero(entre -1000 y 1000)", 10, -1000, 1000)
        case 2:
            print("Salir")
            bandera = False

for i in range(len(lista)):
    print(lista[i], end=" ")