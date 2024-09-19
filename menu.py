from package_arrays.array_generales import *
from os import system

lista = crear_lista(None, 10)
bandera_lista_llena = False
bandera = True
while bandera:
    opcion = get_int("1. Ingresar 10 numeros entre -1000 y 1000\n2. Mostrar la cantidad de numeros positivos y negativos\n3. Mostrar sumatoria de los numeros pares\n4. Salir\nIngrese una opcion: ", "Ingrese una de las opciones arriba mencionadas: ", 1, 4)
    match opcion:
        case 1:
            lista = get_list("Ingrese un numero(entre -1000 y 1000): ", "Reingrese el numero(entre -1000 y 1000)", 10, -1000, 1000)
            bandera_lista_llena = True
        case 2:
            if bandera_lista_llena:
                print(f"Usted ha ingresado {cantidad_positivos} numeros positivos y {cantidad_negativos} numeros negativos.")
            else:
                print("Primero debe ingresar los 10 numeros.")
        case 3:
            if bandera_lista_llena:
                print(f"La suma de los numeros pares ingresados es de {suma_pares}.")
            else:
                print("Primero debe ingresar los 10 numeros.")
        case 4:
            print("Salir")
            bandera = False
    if bandera_lista_llena:
        cantidad_positivos = calcular_positivos(lista)
        cantidad_negativos = calcular_negativos(lista)
        suma_pares = sumar_pares(lista)