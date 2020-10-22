__author__ = 'Dmitry Patashov'

import myFunctions as mf
import numpy as np
import cv2
from matplotlib import pyplot as plt
import logicFunctions as lf

img = cv2.imread('NoisyS.pgm')

GaussMask = 1.0/273 * np.array([[1, 4, 7, 4, 1],
                                [4, 16, 26, 16, 4],
                                [7, 26, 41, 26, 7],
                                [4, 16, 26, 16, 4],
                                [1, 4, 7, 4, 1]])

medImg = lf.MedianSQFilter(img, 10)
gaussMedImg0 = mf.myMasking(lf.myExtendedPadding(np.float64(medImg), 2), GaussMask)

gaussMedImg = gaussMedImg0.copy()
gaussMedImg = gaussMedImg - np.min(gaussMedImg)
gaussMedImg = gaussMedImg * 255 / np.max(gaussMedImg)
gaussMedImg = np.uint8(np.round(gaussMedImg))

plt.figure()

plt.subplot(121)
plt.axis('off')
plt.title('Original image')
plt.imshow(img[:,:,::-1])

plt.subplot(122)
plt.axis('off')
plt.title('Median + Gaussian filtered image')
plt.imshow(gaussMedImg[:,:,::-1])

# Bonus Part
SharpenMask = np.array([[-1, -2, -1],
                        [-2, 13, -2],
                        [-1, -2, -1]])

gaussMedImg1 = mf.myMasking(lf.myExtendedPadding(np.float64(gaussMedImg0)), SharpenMask)

gaussMedImg1[gaussMedImg1 < 0] = 0
gaussMedImg1[gaussMedImg1 > 255] = 255
gaussMedImg1 = np.uint8(np.round(gaussMedImg1))

plt.figure()

plt.subplot(121)
plt.axis('off')
plt.title('Original image')
plt.imshow(img[:,:,::-1])

plt.subplot(122)
plt.axis('off')
plt.title('Median + Gaussian + Sharpen filtered image')
plt.imshow(gaussMedImg1[:,:,::-1])

plt.show()
