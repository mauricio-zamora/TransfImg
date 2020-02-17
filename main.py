from funcionales_generales import *
import os

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

    jpeg_images = os.path.join(nuevo_ds,'JPEGImages')
    if not os.path.exists(jpeg_images):
        os.mkdir(jpeg_images)
    segmentation_class = os.path.join(nuevo_ds,'SegmentationClass')
    if not os.path.exists(segmentation_class):
        os.mkdir(segmentation_class)
    segmentation_object = os.path.join(nuevo_ds,'SegmentationObject')
    if not os.path.exists(segmentation_object):
        os.mkdir(segmentation_object)
    return annotations, image_sets, jpeg_images, segmentation_class, segmentation_object, action, layout

def procesar_data_set(directorio_base):
    directorio_base = verficar_ruta_directorio(directorio_base)
    annotations, image_sets, jpeg_images, segmentation_class, segmentation_object, action, layout = crear_estructura_salida(directorio_base)
    # anotaciones = 'Annotations'
    # imagene_set = 'ImageSets'
    # imagenes_jpg = 'JPEGImages'
    # clases_seg = 'SegmentationClass'
    # obj_seg = 'SegmentationObject'


def main():
    procesar_data_set('/home/mauricio/Escritorio/tools_dataset')

if __name__ == '__main__':
    main()