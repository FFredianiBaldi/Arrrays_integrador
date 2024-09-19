from package_input.validate import *

def get_int(mensaje:str, mensaje_error:str, minimo:int = float("-inf"), maximo:int = float("+inf"), reintentos:int = float("+inf"))->int|None:
    """Funcion que pide un numero y valida que el numero este en un rango

    Args:
        mensaje (str): mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
        mensaje_error (str): mensaje de error en el caso de que el dato ingresado sea invalido.
        minimo (int): valor mínimo admitido (inclusive)
        maximo (int): valor máximo admitido (inclusive)
        reintentos (int): cantidad de veces que se volverá a pedir el dato en caso de error.

    Returns:
        int|None: En caso de que la función no haya podido conseguir un número válido, la misma retorna None.
    """
    bandera_primera_iteracion = True
    while reintentos > 0:
        if bandera_primera_iteracion:
            numero = int(input(mensaje))
        else:
            numero = int(input(mensaje_error))
        if validate_number(numero, minimo, maximo):
            numero = int(numero)
            return numero
        reintentos -= 1
        bandera_primera_iteracion = False
    return None

def get_float(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int)->float|None:
    """Funcion que pide un numero y valida que el numero este en un rango

    Args:
        mensaje (str): mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
        mensaje_error (str): mensaje de error en el caso de que el dato ingresado sea invalido.
        minimo (int): valor mínimo admitido (inclusive)
        maximo (int): valor máximo admitido (inclusive)
        reintentos (int): cantidad de veces que se volverá a pedir el dato en caso de error.

    Returns:
        float|None: En caso de que la función no haya podido conseguir un número válido, la misma retorna None.
    """
    bandera_primera_iteracion = True
    while reintentos > 0:
        if bandera_primera_iteracion:
            numero = float(input(mensaje))
        else:
            numero = float(input(mensaje_error))
        if validate_number(numero, minimo, maximo):
            numero = float(numero)
            return numero
        reintentos -= 1
        bandera_primera_iteracion = False
    return None

def get_string(mensaje:str, mensaje_error:str, minimo:int, reintentos:int)->str|None:
    """Funcion que pide una cadena y valida que la cantidad de caracteres sea mayor al minimo ingresado

    Args:
        mensaje (str): mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
        mensaje_error (str): mensaje de error en el caso de que el dato ingresado sea invalido.
        minimo (int): valor minimo de caracteres.
        reintentos (int): cantidad de veces que se volverá a pedir el dato en caso de error.

    Returns:
        str|None: En caso de que la función no haya podido conseguir una cadena valida, la misma retorna None.
    """
    
    bandera_primera_iteracion = True
    while reintentos > 0:
        if bandera_primera_iteracion:
            palabra = input(mensaje)
        else:
            palabra = input(mensaje_error)
        if validate_length(palabra, minimo):
            return palabra
        reintentos -= 1
        bandera_primera_iteracion = False
    return None

def calcular_promedio_lista(lista:list)->float | None:
    """Funcion que recibe una lista de numeros enteros y retorna el promedio

    Args:
        lista (list): lista de numeros enteros

    Returns:
        float | None: promedio de los numeros de la lista
    """
    acumulador = 0
    for i in range(len(lista)):
        acumulador += lista[i]
    if len(lista) > 0:
        promedio = acumulador / len(lista)
        return promedio
    return None

def calcular_promedio_lista_positivos(lista:list)->float:
    """Funcion que calcula el promedio de numeros enteros y positivos de una lista

    Args:
        lista (list): lista de numeros enteros

    Returns:
        float: promedio de los positivos
    """
    acumulador = 0
    contador_positivos = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            acumulador += lista[i]
            contador_positivos += 1
    if contador_positivos > 0:
        promedio = acumulador / contador_positivos
        return promedio
    return 0

def calcular_producto_lista(lista:list)->int:
    """Funcion que calcula el producto de los numeros de una lista

    Args:
        lista (list): lista de numeros enteros

    Returns:
        int: producto de los numeros de la lista
    """
    producto = 1
    for i in range(len(lista)):
        producto *= lista[i]
    if len(lista) > 0:
        return producto
    return 0

def calcular_posicion_lista_maximo(lista:list)->int:
    """Funcion que retorna la posicion del numero mas alto en una lista

    Args:
        lista (list): lista de numeros enteros

    Returns:
        int: posicion del numero mas alto en esa lista
    """
    maximo_numero = lista[0]
    maximo_posicion = 0
    for i in range(1, len(lista)):
        if lista[i] > maximo_numero:
            maximo_numero = lista[i]
            maximo_posicion = i
    
    return maximo_posicion

def calcular_posiciones_lista_maximo(lista:list)->list:
    """Funcion que calcula en que posicion/posiciones se encuentra el numero mas alto de una lista

    Args:
        lista (list): lista de numeros a procesar

    Returns:
        list: lista con las posiciones donde se encuentra el numero mas alto
    """
    maximo_numero = lista[0]
    lista_maximos = []
    for i in range(len(lista)):
        if lista[i] >= maximo_numero:
            maximo_numero = lista[i]
    for i in range(len(lista)):
        if lista[i] == maximo_numero:
            lista_maximos += [i]
    
    return lista_maximos

def reemplazar_nombre(lista_nombres:list, nombre_reemplazar:str, reemplazo:str)->int:
    """Funcion que reemplaza un nombre de una lista con el nombre deseado

    Args:
        lista_nombres (list): lista de nombres
        nombre_reemplazar (str): nombre a reemplazar
        reemplazo (str): reemplazo del nombre

    Returns:
        int: cantidad de reemplazos realizados
    """
    contador_reemplazos = 0
    for i in range(len(lista_nombres)):
        if lista_nombres[i] == nombre_reemplazar:
            lista_nombres[i] = reemplazo
            contador_reemplazos += 1
    
    return contador_reemplazos

def mostrar_lista(lista:list, excepcion:any):
    for i in range(len(lista)):
        if lista[i] != excepcion:
            print(f"Elemento {i+1}: {lista[i]}")

def acumular_lista(lista:list, excepcion:any):
    acumulador = 0
    for i in range(len(lista)):
        if lista[i] != excepcion:
            acumulador += lista[i]
    return acumulador