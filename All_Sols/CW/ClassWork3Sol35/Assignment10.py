__author__ = 'Dmitry Patashov'

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img1.jpg')
im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

im1 = np.float64(im) - 50
im2 = np.float64(im) + 50

im1[im1<0] = 0
im2[im2 > 255] = 255

im1 = np.uint8(im1)
im2 = np.uint8(im2)

plt.figure()
p1 = plt.subplot(132)
p1.title.set_text('Original Image')
plt.imshow(im, cmap='gray')

p2 = plt.subplot(131)
p2.title.set_text('Image - 50')
plt.imshow(im1, cmap='gray')

p3 = plt.subplot(133)
p3.title.set_text('Image + 50')
plt.imshow(im2, cmap='gray')

plt.show()
