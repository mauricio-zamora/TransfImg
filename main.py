from funcionales_generales import *
from procesador_anotaciones import *
import os
import glob
import xml.etree.ElementTree as ET
from annotation import *

def listar_nombre_archivos(ruta_origen):
    archivos_anotaciones = [f.split('/')[-1] for f in glob.glob(ruta_origen + '/*.xml')]
    listado_anotaciones = [ l[:l.find('.xml')] for l in archivos_anotaciones]
    return listado_anotaciones


def crear_estructura_salida(directorio_base):
    nuevo_ds = os.path.join(directorio_base,'nuevo_ds')
    if not os.path.exists(nuevo_ds):
        os.mkdir(nuevo_ds)
    annotations = os.path.join(nuevo_ds,'Annotations')
    if not os.path.exists(annotations):
        os.mkdir(annotations)
    image_sets = os.path.join(nuevo_ds,'ImageSets')
    if not os.path.exists(image_sets):
        os.mkdir(image_sets)

    action = os.path.join(image_sets,'Action')
    if not os.path.exists(action):
        os.mkdir(action)
    layout = os.path.join(image_sets,'Layout')
    if not os.path.exists(layout):
        os.mkdir(layout)
    main = os.path.join(image_sets,'Main')
    if not os.path.exists(main):
        os.mkdir(main)
    segmentation = os.path.join(image_sets,'Segmentation')
    if not os.path.exists(segmentation):
        os.mkdir(segmentation)

    jpeg_images = os.path.join(nuevo_ds,'JPEGImages')
    if not os.path.exists(jpeg_images):
        os.mkdir(jpeg_images)
    segmentation_class = os.path.join(nuevo_ds,'SegmentationClass')
    if not os.path.exists(segmentation_class):
        os.mkdir(segmentation_class)
    segmentation_object = os.path.join(nuevo_ds,'SegmentationObject')
    if not os.path.exists(segmentation_object):
        os.mkdir(segmentation_object)
    return annotations, image_sets, jpeg_images, segmentation_class, segmentation_object, action, layout, main, segmentation

def procesar_data_set(directorio_base):
    directorio_base = verficar_ruta_directorio(directorio_base)
    main_annotations = os.path.join(directorio_base, 'Annotations')
    annotations, image_sets, jpeg_images, segmentation_class, segmentation_object, action, layout, main, segmentation = crear_estructura_salida(directorio_base)
    elementos_procesar = listar_nombre_archivos(main_annotations)
    lista_anots, lista_clases = listar_anotaciones(directorio_base, elementos_procesar)
    mapa_clases = generar_mapeo_clases(lista_anots, lista_clases)
    for k, v in mapa_clases.items():
        for k2, v2 in v.items():
            print(k, '*', k2, '*', v2)

def main():
    procesar_data_set('/home/mauricio/Escritorio/tools_dataset')



if __name__ == '__main__':
    main()