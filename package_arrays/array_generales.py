from package_arrays.especificas import *
from package_arrays.package_input.input import *
def get_list(mensaje:str, mensaje_error:str, cantidad_numeros:int, minimo:int = float("-inf"), maximo:int = float("+inf"), reintentos:int = float("+inf")):
    lista = [None] * cantidad_numeros
    for i in range(cantidad_numeros):
        lista[i] = get_int(mensaje, mensaje_error, minimo, maximo, reintentos)
    
    return lista