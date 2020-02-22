import matplotlib.pyplot as plt
import numpy as np
import cv2

image = cv2.imread('bolt-00000.jpg')
print('This image is:', type(image),
      ' with dimensions:', image.shape)

image_copy = np.copy(image)
plt.imshow(image_copy)
plt.show()

image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)
plt.imshow(image_copy)
plt.show()

lower_white = np.array([235, 235, 235])
upper_white = np.array([255, 255, 255])

mask = cv2.inRange(image_copy, lower_white, upper_white)
plt.imshow(mask, cmap='gray')
plt.show()

masked_image = np.copy(image_copy)
masked_image[mask != 0] = [0, 0, 0]
plt.imshow(masked_image)
plt.show()