from package_arrays.especificas import *
from package_arrays.package_input.input import *
def get_list(mensaje:str, mensaje_error:str, cantidad_numeros:int, minimo:int = float("-inf"), maximo:int = float("+inf"), reintentos:int = float("+inf")):
    lista = [None] * cantidad_numeros
    for i in range(cantidad_numeros):
        lista[i] = get_int(mensaje, mensaje_error, minimo, maximo, reintentos)
    
    return lista

def calcular_positivos(lista:list)->int:
    contador_positivos = 0
    for i in range(len(lista)):
        if determinar_positivo(lista[i]):
            contador_positivos += 1
    return contador_positivos

def calcular_negativos(lista:list)->int:
    contador_negativos = 0
    for i in range(len(lista)):
        if determinar_positivo(lista[i]) == False:
            contador_negativos += 1
    return contador_negativos

def sumar_pares(lista:list)->int:
    acumulador_pares = 0
    for i in range(len(lista)):
        if determinar_par(lista[i]):
            acumulador_pares += lista[i]
    return acumulador_pares