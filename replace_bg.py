import matplotlib.pyplot as plt
import numpy as np
import cv2
import random


def cambiar_fondo_aleatorio(imagen):
    fondos_metal = ['bgmetal00.jpg', 'bgmetal01.jpg', 'bgmetal02.jpg', 'bgmetal03.jpg', 'bgmetal04.jpg',
                    'bgmetal05.jpg', 'bgmetal06.jpg', 'bgmetal07.jpg', 'bgmetal08.jpg', 'bgmetal09.jpg']
    fondos_madera = ['bgmadera00.jpg', 'bgmadera01.jpg', 'bgmadera02.jpg', 'bgmadera03.jpg', 'bgmadera04.jpg',
                     'bgmadera05.jpg', 'bgmadera06.jpg', 'bgmadera07.jpg', 'bgmadera08.jpg', 'bgmadera09.jpg']
    fondos_textura = ['bgtextura00.jpg', 'bgtextura01.jpg', 'bgtextura02.jpg', 'bgtextura03.jpg', 'bgtextura04.jpg',
                      'bgtextura05.jpg', 'bgtextura06.jpg', 'bgtextura07.jpg', 'bgtextura08.jpg', 'bgtextura09.jpg']
    random.seed()

    # random.shuffle(fondos_metal)
    # random.shuffle(fondos_madera)
    # random.shuffle(fondos_textura)
    ifondo = random.randint(0, 2)
    iframe = random.randint(0, 9)
    if ifondo == 0:
        fondo = fondos_metal[iframe]
    elif ifondo == 1:
        fondo = fondos_madera[iframe]
    else:
        fondo = fondos_textura[iframe]
    print(fondo)
    # random.seed()
    # fondo = random.choice(fondos_madera)
    background_image = cv2.imread(fondo)
    return cambiar_fondo(imagen, background_image)


def cambiar_fondo(imagen, fondo):
    image_copy = np.copy(imagen)
    # image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)
    lower_white = np.array([235, 235, 235])
    upper_white = np.array([255, 255, 255])
    mask = cv2.inRange(image_copy, lower_white, upper_white)
    masked_image = np.copy(image_copy)
    masked_image[mask != 0] = [0, 0, 0]
    background_image = fondo
    # background_image = cv2.cvtColor(fondo, cv2.COLOR_BGR2RGB
    crop_background = background_image[0:500, 0:500]
    crop_background[mask == 0] = [0, 0, 0]
    complete_image = masked_image + crop_background
    return complete_image


def main():
    # lista_fondos = ['bgmetal0' + str(i) + '.jpg' for i in range(10)] + ['bgmadera0' + str(i) + '.jpg' for i in range(10)] + ['bgtextura0' + str(i) + '.jpg' for i in range(10)]
    # print(lista_fondos)
    # fondo = random.choice(lista_fondos)
    image = cv2.imread('bolt-00000.jpg')
    # background_image = cv2.imread(fondo)
    # img = cambiar_fondo(image, background_image)
    img = cambiar_fondo_aleatorio(image)
    plt.imshow(img)
    plt.show()


if __name__ == '__main__':
    main()
# image = cv2.imread('bolt-00000.jpg')
# print('This image is:', type(image),
#       ' with dimensions:', image.shape)
#
# image_copy = np.copy(image)
# plt.imshow(image_copy)
# plt.show()
#
# image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)
# plt.imshow(image_copy)
# plt.show()
#
# lower_white = np.array([235, 235, 235])
# upper_white = np.array([255, 255, 255])
#
# mask = cv2.inRange(image_copy, lower_white, upper_white)
# plt.imshow(mask, cmap='gray')
# plt.show()
#
# masked_image = np.copy(image_copy)
# masked_image[mask != 0] = [0, 0, 0]
# plt.imshow(masked_image)
# plt.show()
#
# background_image = cv2.imread('bgmadera00.jpg')
# background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB)
# crop_background = background_image[0:514, 0:816]
#
# crop_background[mask == 0] = [0,0,0]
# plt.imshow(crop_background)
# plt.show()
#
# complete_image = masked_image + crop_background
# plt.imshow(complete_image)
# plt.show()
