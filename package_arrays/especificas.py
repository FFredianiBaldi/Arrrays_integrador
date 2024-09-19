def determinar_positivo(numero:int)->bool:
    if numero >= 0:
        return True
    return False

def determinar_par(numero:int)->bool:
    if numero % 2 == 0:
        return True
    return False

def determinar_mayor(lista:list)->int:
    maximo_numero = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > maximo_numero:
            maximo_numero = lista[i]
    
    return maximo_numero