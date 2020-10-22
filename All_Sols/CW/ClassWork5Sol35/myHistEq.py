__author__ = 'Dmitry Patashov'

import os
import cv2
from matplotlib import pyplot as plt
import myHistEqLogic as mhe

CurDir = os.getcwd()
ImgAdd = CurDir + '\Images\\'

Img = cv2.imread(ImgAdd + 'Dark Image.jpg')
# Img = cv2.imread(ImgAdd + 'Giraffe.jpg')

RepImg = mhe.myHistEqualization(Img)

plt.figure()
plt.subplot(221)
plt.title('Original Image')
plt.axis('off')
plt.imshow(Img, vmin = 0, vmax = 255)
plt.subplot(222)
plt.title('Histogram Equalization')
plt.axis('off')
plt.imshow(RepImg, vmin = 0, vmax = 255)

plt.subplot(223)
plt.hist(Img.ravel(), bins=256, range=(0.0, 256), facecolor='black')
plt.xlim([0,256])
plt.subplot(224)
plt.hist(RepImg.ravel(), bins=256, range=(0.0, 256), facecolor='blue')
plt.xlim([0,256])

plt.show()
