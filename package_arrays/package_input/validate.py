def validate_number(numero:int, minimo:int, maximo:int)->float|None:
    if numero >= minimo and numero <= maximo:
        return True
    else:
        return False

def validate_length(palabra, minimo):
    if len(palabra) >= minimo:
        return True
    else:
        return False