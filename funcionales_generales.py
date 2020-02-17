def texto_es_none(texto, salida=''):
    valor = salida
    if texto is not None:
        valor = texto
    return valor


def numero_es_none(texto, salida=-1):
    valor = salida
    if texto is not None:
        valor = texto
    return valor

def verficar_ruta_directorio(ruta):
    if (ruta[-1] != '/'):
        salida = ruta + '/'
    else:
        salida = ruta
    return salida