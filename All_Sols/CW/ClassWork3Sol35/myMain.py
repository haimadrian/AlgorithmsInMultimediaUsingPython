__author__ = 'Dmitry Patashov'

import myFunctions as mf
import cv2
from matplotlib import pyplot as plt

img0 = cv2.imread('img1.jpg', 0)
img1 = cv2.imread('img1.jpg')
img2 = cv2.imread('img2.jpg')
img3 = cv2.imread('img3.png')
img4 = cv2.imread('img4.jpeg')

# Assignment 3:

cv2.imshow('BGR', img4)

plt.figure('RGB')
plt.imshow(mf.myBGR2RGB(img4.copy()))

plt.show()
cv2.waitKey()


# Assignment 5:

plt.figure()
plt.subplot(121)
plt.imshow(mf.myGreenLine(img4.copy())[:,:,::-1])
plt.subplot(122)
plt.imshow(mf.myGreenLine(img0.copy(), 75))
plt.show()


# Assignment 6:

plt.figure()
plt.subplot(131)
plt.imshow(mf.myRedLine(img0.copy())[:,:,::-1])
plt.subplot(132)
plt.imshow(mf.myRedLine(img4.copy(), 50)[:,:,::-1])
plt.subplot(133)
plt.imshow(mf.myRedLine(img4[:,:,::-1].copy(), 75, 'RGB')[:,:,::-1])
plt.show()


# Assignment 7:

plt.figure()
plt.subplot(131)
plt.imshow(mf.myBlueSquare(img0.copy())[:,:,::-1])
plt.subplot(132)
plt.imshow(mf.myBlueSquare(img4.copy(), 50)[:,:,::-1])
plt.subplot(133)
plt.imshow(mf.myBlueSquare(img4[:,:,::-1].copy(), 75, 'RGB')[:,:,::-1])
plt.show()


# Assignment 8:

plt.figure()
plt.subplot(121)
plt.imshow(mf.myPurpleCircle(img0.copy())[:,:,::-1])
plt.subplot(122)
plt.imshow(mf.myPurpleCircle(img4.copy(), 30)[:,:,::-1])
plt.show()


# Assignment 9:

plt.figure()
plt.subplot(121)
plt.imshow(mf.myColorfullTriangle(img0.copy())[:,:,::-1])
plt.subplot(122)
plt.imshow(mf.myColorfullTriangle(img1.copy())[:,:,::-1])
plt.show()


# Assignment 11:

plt.figure()
plt.subplot(121)
plt.imshow(mf.myZeroPadding(img0.copy(), 100), cmap='gray')
plt.subplot(122)
plt.imshow(mf.myZeroPadding(img1.copy(), 50)[:,:,::-1])
plt.show()


# Assignment 12:

plt.figure()
plt.subplot(121)
plt.axis('off')
plt.imshow(mf.myExtendedPadding(img0.copy(), 100), cmap='gray')
plt.subplot(122)
plt.axis('off')
plt.imshow(mf.myExtendedPadding(img1.copy(), 50)[:,:,::-1])
plt.show()


# Assignment 13:

plt.figure()
plt.subplot(121)
plt.axis('off')
plt.imshow(mf.GradientEdgeDetector(img0.copy()), cmap='gray')
plt.subplot(122)
plt.axis('off')
plt.imshow(mf.GradientEdgeDetector(img3.copy())[:,:,::-1])
plt.show()
