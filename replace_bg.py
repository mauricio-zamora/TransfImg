import matplotlib.pyplot as plt
import numpy as np
import cv2
import random


def cambiar_fondo(imagen, fondo):
      image_copy = np.copy(imagen)
      image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)
      lower_white = np.array([235, 235, 235])
      upper_white = np.array([255, 255, 255])
      mask = cv2.inRange(image_copy, lower_white, upper_white)
      masked_image = np.copy(image_copy)
      masked_image[mask != 0] = [0, 0, 0]
      background_image = cv2.cvtColor(fondo, cv2.COLOR_BGR2RGB)
      crop_background = background_image[0:500, 0:500]
      crop_background[mask == 0] = [0, 0, 0]
      complete_image = masked_image + crop_background
      return complete_image


def main():
      image = cv2.imread('bolt-00000.jpg')
      background_image = cv2.imread('bgmadera00.jpg')
      img = cambiar_fondo(image, background_image)
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
