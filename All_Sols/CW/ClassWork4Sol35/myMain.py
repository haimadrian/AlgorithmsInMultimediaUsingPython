__author__ = 'Dmitry Patashov'

import myFunctions as mf
import numpy as np
import cv2
from matplotlib import pyplot as plt
import logicFunctions as lf

img1 = cv2.imread('img1.jpg')
img3 = cv2.imread(('BlurryImage1.jpg'))

# Assignment 1:

GaussMask = 1.0/273 * np.array([[1, 4, 7, 4, 1],
                                [4, 16, 26, 16, 4],
                                [7, 26, 41, 26, 7],
                                [4, 16, 26, 16, 4],
                                [1, 4, 7, 4, 1]])

LaplacianMask = np.array([[0, -1, 0],
                          [-1, 4, -1],
                          [0, -1, 0]])

GFmat = mf.myMasking(lf.myExtendedPadding(img1.copy()), GaussMask)
LFmat = mf.myMasking(lf.myExtendedPadding(img1.copy()), LaplacianMask)

GFmat2 = GFmat - np.min(GFmat)
GFimg = np.uint8(np.round(GFmat2 * 255 / np.max(GFmat2)))

LFmat2 = np.abs(LFmat)
LFmat2 = LFmat2 - np.min(LFmat2)
LFimg = np.uint8(np.round(LFmat2 * 255 / np.max(LFmat2)))

plt.figure()
plt.subplot(221)
plt.axis('off')
plt.title('Original image')
plt.imshow(img1[:,:,::-1])

plt.subplot(222)
plt.axis('off')
plt.title('Gaussian filtered image')
plt.imshow(GFimg[:,:,::-1])

plt.subplot(223)
plt.axis('off')
plt.title('Laplacian filtered image')
plt.imshow(LFimg[:,:,::-1])

plt.subplot(224)
plt.axis('off')
plt.title('Laplacian filtered image')
plt.imshow(np.max(LFimg, axis=2), cmap='gray')

plt.show()


# Assignment 2:

myMask = np.array([[-1, -1, -1],
                   [-1, 10, -1],
                   [-1, -1, -1]])

Mimg = np.uint8(np.round(np.abs(mf.myMasking(lf.myExtendedPadding(img3.copy()), myMask))))

plt.figure()
plt.subplot(121)
plt.axis('off')
plt.title('Original image')
plt.imshow(img3[:,:,::-1])

plt.subplot(122)
plt.axis('off')
plt.title('Masked image')
plt.imshow(Mimg[:,:,::-1])

plt.show()


# Assignment 3:

img3g = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
Mimgg = cv2.cvtColor(Mimg, cv2.COLOR_BGR2GRAY)

hist1 = mf.myHistPlotUint8(img3g)
hist2 = mf.myHistPlotUint8(Mimgg)

plt.figure()
plt.subplot(121)
plt.title('Original image')
plt.bar(range(256), hist1)

plt.subplot(122)
plt.title('Masked image')
plt.bar(range(256), hist2)

plt.figure()
plt.subplot(121)
plt.title('Original image')
plt.bar(range(256), hist1)
plt.ylim((0, np.max(hist1) / 20))

plt.subplot(122)
plt.title('Masked image')
plt.bar(range(256), hist2)
plt.ylim((0, np.max(hist2) / 20))

plt.show()
