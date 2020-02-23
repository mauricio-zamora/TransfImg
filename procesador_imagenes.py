# https://www.pyimagesearch.com/2017/01/02/rotate-images-correctly-with-opencv-and-python/
# https://github.com/jrosebr1/imutils
import numpy as np
import argparse
import imutils
import cv2
import glob
import os
import shutil
from replace_bg import *


def leer_imagen(nombre):
    img = cv2.imread(nombre)
    return cambiar_fondo_aleatorio(img)


def salvar_imagen(imagen, nombre):
    cv2.imwrite(nombre, imagen)


def rotar_90(imagen):
    img_rotada = imutils.rotate_bound(imagen, 90)
    return img_rotada, '_rot90'


def rotar_180(imagen):
    img_rotada = imutils.rotate_bound(imagen, 180)
    return img_rotada, '_rot180'


def rotar_270(imagen):
    img_rotada = imutils.rotate_bound(imagen, 270)
    return img_rotada, '_rot270'


def transladar(imagen, x=0, y=0):
    img_traslada = imutils.translate(imagen, x, -1 * y)
    sufijo = '_tranx{:d}y{:d}'.format(x, y)
    return img_traslada, sufijo


def cannyficar(imagen):
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    canificada = imutils.auto_canny(gray)
    return canificada, '_canf'


def cannyficar2(imagen):
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    canificada = cv2.Canny(gray, 20, 100)
    return canificada, '_canf'


def voltearVertical(imagen):
    volteada = cv2.flip(imagen, 0)
    return volteada, '_flipv'


def voltearHorizontal(imagen):
    volteada = cv2.flip(imagen, 1)
    return volteada, '_fliph'


def transformar_archivo(ruta_origen, ruta_destino, nombre_archivo,
                        rotar90=True, rotar180=True, rotar270=True,
                        trasladarxy=True, x=0, y=0,
                        canificada=True, volvert=True, volhort=True):
    i = nombre_archivo.find(".")
    archivo_nombre = nombre_archivo[:i]
    archivo_extension = nombre_archivo[i + 1:]
    origen = ruta_origen + nombre_archivo
    destino = ruta_destino + archivo_nombre + '{}' + '.' + archivo_extension
    img = leer_imagen(origen)
    if rotar90:
        nimg, sufijo = rotar_90(img)
        na = destino.format(sufijo)
        salvar_imagen(nimg, na)
    if rotar180:
        nimg, sufijo = rotar_180(img)
        na = destino.format(sufijo)
        salvar_imagen(nimg, na)
    if rotar270:
        nimg, sufijo = rotar_270(img)
        na = destino.format(sufijo)
        salvar_imagen(nimg, na)
    if trasladarxy:
        nimg, sufijo = transladar(img, x, y)
        na = destino.format(sufijo)
        salvar_imagen(nimg, na)
    if canificada:
        nimg, sufijo = cannyficar2(img)
        na = destino.format(sufijo)
        salvar_imagen(nimg, na)
    if volvert:
        nimg, sufijo = voltearVertical(img)
        na = destino.format(sufijo)
        salvar_imagen(nimg, na)
    if volhort:
        nimg, sufijo = voltearHorizontal(img)
        na = destino.format(sufijo)
        salvar_imagen(nimg, na)


def listar_archivos(ruta_origen, ruta_destino):
    nombres_anotaciones = [f for f in glob.glob(ruta_origen + '/*.jpg')]
    for nombre_anotacion in nombres_anotaciones:
        nombre_archivo = nombre_anotacion.split('/')[-1]
        ruta_anotacion = nombre_anotacion[:len(nombre_archivo) * -1]
        transformar_archivo(ruta_origen=ruta_anotacion, ruta_destino=ruta_destino, nombre_archivo=nombre_archivo, x=50,
                            y=50)
        # copiar_archivos(ruta_anotacion, ruta_destino,nombre_archivo,'_1')


def copiar_archivos(ruta_origen, ruta_destino, nombre_archivo, sufijo=''):
    i = nombre_archivo.find(".")
    archivo_nombre = nombre_archivo[:i]
    archivo_extension = nombre_archivo[i + 1:]
    origen = ruta_origen + nombre_archivo
    destino = ruta_destino + archivo_nombre + sufijo + '.' + archivo_extension
    resultado = shutil.copyfile(origen, destino)
    print('Salida: {:_^90}'.format(resultado))


def main():
    listar_archivos('/home/mauricio/Escritorio/tools_dataset/JPEGImages',
                    '/home/mauricio/Escritorio/tools_dataset/NewImages/')


if __name__ == '__main__':
    main()
