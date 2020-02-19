from funcionales_generales import *
from procesador_anotaciones import *
import xml.etree.ElementTree as ET
from annotation import *
from procesador_yolo_anotacion_lxml import *
from xml.dom import minidom
import glob
import os
from copy import deepcopy
import shutil
from procesador_imagenes import *


def listar_nombre_archivos(ruta_origen):
    archivos_anotaciones = [f.split('/')[-1] for f in glob.glob(ruta_origen + '/*.xml')]
    listado_anotaciones = [l[:l.find('.xml')] for l in archivos_anotaciones]
    return listado_anotaciones


def crear_estructura_salida(directorio_base):
    nuevo_ds = os.path.join(directorio_base, 'nuevo_ds')
    if not os.path.exists(nuevo_ds):
        os.mkdir(nuevo_ds)
    annotations = os.path.join(nuevo_ds, 'Annotations')
    if not os.path.exists(annotations):
        os.mkdir(annotations)
    image_sets = os.path.join(nuevo_ds, 'ImageSets')
    if not os.path.exists(image_sets):
        os.mkdir(image_sets)

    action = os.path.join(image_sets, 'Action')
    if not os.path.exists(action):
        os.mkdir(action)
    layout = os.path.join(image_sets, 'Layout')
    if not os.path.exists(layout):
        os.mkdir(layout)
    main = os.path.join(image_sets, 'Main')
    if not os.path.exists(main):
        os.mkdir(main)
    segmentation = os.path.join(image_sets, 'Segmentation')
    if not os.path.exists(segmentation):
        os.mkdir(segmentation)

    jpeg_images = os.path.join(nuevo_ds, 'JPEGImages')
    if not os.path.exists(jpeg_images):
        os.mkdir(jpeg_images)
    segmentation_class = os.path.join(nuevo_ds, 'SegmentationClass')
    if not os.path.exists(segmentation_class):
        os.mkdir(segmentation_class)
    segmentation_object = os.path.join(nuevo_ds, 'SegmentationObject')
    if not os.path.exists(segmentation_object):
        os.mkdir(segmentation_object)
    return annotations, image_sets, jpeg_images, segmentation_class, segmentation_object, action, layout, main, segmentation


def procesar_data_set(directorio_base):
    directorio_base = verficar_ruta_directorio(directorio_base)
    main_annotations = os.path.join(directorio_base, 'Annotations')
    main_jpeg_images = os.path.join(directorio_base, 'JPEGImages')
    annotations, image_sets, jpeg_images, segmentation_class, segmentation_object, action, layout, main, segmentation = crear_estructura_salida(
        directorio_base)
    elementos_procesar = listar_nombre_archivos(main_annotations)
    lista_anots, lista_clases = listar_anotaciones(directorio_base, elementos_procesar)
    for nombre_elemento, anotacion_cruda in lista_anots.items():
        # Archivo base
        anotacion_base = reprocesar_anotacion(anotacion_cruda)
        xml_anotacion_base = regenerarxml(anotacion_base)
        escribir_xml(xml_anotacion_base, os.path.join(annotations, nombre_elemento + '.xml'))
        shutil.copyfile(os.path.join(main_jpeg_images, nombre_elemento + '.jpg'),
                        os.path.join(jpeg_images, nombre_elemento + '.jpg'))
        destino = nombre_elemento + '{}' + '.jpg'
        # ROTAR 90 - Inicio
        img = leer_imagen(os.path.join(jpeg_images, nombre_elemento + '.jpg'))
        nimg, sufijo = rotar_90(img)
        na = destino.format(sufijo)
        anotacion_rota90 = reprocesar_anotacion(anotacion_cruda)
        anotacion_rota90.filename = nombre_elemento + sufijo + '.jpg'
        for o in anotacion_rota90.objects:
            x1 = o.bndbox['xmin']
            y1 = o.bndbox['ymin']
            x2 = o.bndbox['xmax']
            y2 = o.bndbox['ymax']
            o.bndbox['xmin'] = str(500 - int(y2))
            o.bndbox['ymin'] = x1
            o.bndbox['xmax'] = str(500 - int(y1))
            o.bndbox['ymax'] = x2
        xml_anotacion_rota90 = regenerarxml(anotacion_rota90)
        escribir_xml(xml_anotacion_rota90, os.path.join(annotations, nombre_elemento + sufijo + '.xml'))
        salvar_imagen(nimg, os.path.join(jpeg_images, na))
        # ROTAR 90 - Fin
        # ROTAR 180 - Inicio
        img = leer_imagen(os.path.join(jpeg_images, nombre_elemento + '.jpg'))
        nimg, sufijo = rotar_180(img)
        na = destino.format(sufijo)
        anotacion_rota180 = reprocesar_anotacion(anotacion_cruda)
        anotacion_rota180.filename = nombre_elemento + sufijo + '.jpg'
        for o in anotacion_rota180.objects:
            x1 = o.bndbox['xmin']
            y1 = o.bndbox['ymin']
            x2 = o.bndbox['xmax']
            y2 = o.bndbox['ymax']
            o.bndbox['xmin'] = str(500 - int(x2))
            o.bndbox['ymin'] = str(500 - int(y2))
            o.bndbox['xmax'] = str(500 - int(x1))
            o.bndbox['ymax'] = str(500 - int(y1))
        xml_anotacion_rota180 = regenerarxml(anotacion_rota180)
        escribir_xml(xml_anotacion_rota180, os.path.join(annotations, nombre_elemento + sufijo + '.xml'))
        salvar_imagen(nimg, os.path.join(jpeg_images, na))
        # ROTAR 180 - Fin
        # ROTAR 270 - Inicio
        img = leer_imagen(os.path.join(jpeg_images, nombre_elemento + '.jpg'))
        nimg, sufijo = rotar_270(img)
        na = destino.format(sufijo)
        anotacion_rota270 = reprocesar_anotacion(anotacion_cruda)
        anotacion_rota270.filename = nombre_elemento + sufijo + '.jpg'
        for o in anotacion_rota270.objects:
            x1 = o.bndbox['xmin']
            y1 = o.bndbox['ymin']
            x2 = o.bndbox['xmax']
            y2 = o.bndbox['ymax']
            o.bndbox['xmin'] = y1
            o.bndbox['ymin'] = str(500 - int(x2))
            o.bndbox['xmax'] = y2
            o.bndbox['ymax'] = str(500 - int(x1))
        xml_anotacion_rota270 = regenerarxml(anotacion_rota270)
        escribir_xml(xml_anotacion_rota270, os.path.join(annotations, nombre_elemento + sufijo + '.xml'))
        salvar_imagen(nimg, os.path.join(jpeg_images, na))
        # ROTAR 270 - Fin
        # CANNYFICAR - Inicio
        img = leer_imagen(os.path.join(jpeg_images, nombre_elemento + '.jpg'))
        nimg, sufijo = cannyficar2(img)
        na = destino.format(sufijo)
        anotacion_cann = reprocesar_anotacion(anotacion_cruda)
        anotacion_cann.filename = nombre_elemento + sufijo + '.jpg'

        xml_anotacion_cann = regenerarxml(anotacion_cann)
        escribir_xml(xml_anotacion_cann, os.path.join(annotations, nombre_elemento + sufijo + '.xml'))
        salvar_imagen(nimg, os.path.join(jpeg_images, na))
        # CANNYFICAR - Fin

        # TRASLADAR - Inicio
        img = leer_imagen(os.path.join(jpeg_images, nombre_elemento + '.jpg'))
        offset_x = 100
        offset_y = 100
        nimg, sufijo = transladar(img, offset_x, offset_y)
        na = destino.format(sufijo)
        anotacion_trans = reprocesar_anotacion(anotacion_cruda)
        anotacion_trans.filename = nombre_elemento + sufijo + '.jpg'
        for o in anotacion_trans.objects:
            x1 = o.bndbox['xmin']
            y1 = o.bndbox['ymin']
            x2 = o.bndbox['xmax']
            y2 = o.bndbox['ymax']
            o.bndbox['xmin'] = str(sumar_enteros_dentro_limite(x1, offset_x, 500))
            o.bndbox['ymin'] = str(restar_enteros_dentro_limite(y1, offset_x, 0))
            o.bndbox['xmax'] = str(sumar_enteros_dentro_limite(x2, offset_x, 500))
            o.bndbox['ymax'] = str(restar_enteros_dentro_limite(y2, offset_x, 0))
        xml_anotacion_trans = regenerarxml(anotacion_trans)
        escribir_xml(xml_anotacion_trans, os.path.join(annotations, nombre_elemento + sufijo + '.xml'))
        salvar_imagen(nimg, os.path.join(jpeg_images, na))
        # TRASLADAR - Fin

    # mapa_clases = generar_mapeo_clases(lista_anots, lista_clases)


def main():
    procesar_data_set('/home/mauricio/Escritorio/tools_dataset')


if __name__ == '__main__':
    main()
