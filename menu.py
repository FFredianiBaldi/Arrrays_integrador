from package_arrays.array_generales import *
from os import system

lista = crear_lista(None, 10)
bandera_lista_llena = False
bandera = True
while bandera:
    opcion = get_int("1. Ingresar 10 numeros entre -1000 y 1000\n2. Mostrar la cantidad de numeros positivos y negativos\n3. Mostrar sumatoria de los numeros pares\n4. Mostrar el mayor de los numeros impares\n5. Mostrar todos los numeros ingresados\n6. Mostrar numeros pares\n7. Salir\nIngrese una opcion: ", "Ingrese una de las opciones arriba mencionadas: ", 1, 7)
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
            if bandera_lista_llena:
                if mayor_impares != None:
                    print(f"El mayor de los numeros impares ingresados es el numero {mayor_impares}.")
                else:
                    print("No ingreso ningun numero impar.")
            else:
                print("Primero debe ingresar los 10 numeros.")
        case 5:
            if bandera_lista_llena:
                mostrar_lista(lista, None)
            else:
                print("Primero debe ingresar los 10 numeros.")
        case 6:
            if bandera_lista_llena:
                if numeros_pares != None:
                    print("Los numeros pares ingresados son los siguientes:")
                    for i in range(len(numeros_pares)):
                        print(numeros_pares[i])
                else:
                    print("No ingreso ningun numero par")
            else:
                print("Primero debe ingresar los 10 numeros.")
        case 7:
            print("Salir")
            bandera = False
    if bandera_lista_llena:
        cantidad_positivos = calcular_positivos(lista)
        cantidad_negativos = calcular_negativos(lista)
        suma_pares = sumar_pares(lista)
        mayor_impares = determinar_mayor_impares(lista)
        numeros_pares = buscar_numeros_pares(lista)