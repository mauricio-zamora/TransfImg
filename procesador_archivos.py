import glob

def leer_archivo(archivo):
    f = open(archivo, "r")
    salida = f.readlines()
    f.close()
    return salida


def procesar_lineas(lineas, sufijos):
    salida = []
    for linea in lineas:
        sublineas = linea[:-1].split(' ')
        for sufijo in sufijos:
            tmp = sublineas[0] + sufijo
            if len(sublineas) == 2:
                salida.append(tmp + ' ' + str(sublineas[1]))
            else:
                salida.append(tmp + ' ' + str(sublineas[2]))
    return salida


def escribir_archivo_lineas(archivo, lineas):
    f = open(archivo, "w")  # write mode
    for linea in lineas:
        f.write(linea + '\n')
    f.close()


def listar_archivos_texto(direcotorio_base):
    nombres_archivos = [f for f in glob.glob(direcotorio_base + '/*.txt')]
    archivos = [a.split('/')[-1] for a in nombres_archivos]
    return archivos


def main():
    #lineas = leer_archivo('/home/mauricio/Escritorio/tools_dataset/ImageSets/Main/screw_train.txt')
    #ls = procesar_lineas(lineas,['_canf','_rot90','_rot180','_rot270','_tranx100y100'])
    #escribir_archivo_lineas('/home/mauricio/Escritorio/tools_dataset/nuevo_ds/ImageSets/Main/screw_train.txt', ls)
    fs = listar_archivos_texto('/home/mauricio/Escritorio/tools_dataset/ImageSets/Main/')
    print(fs)

if __name__ == '__main__':
    main()
