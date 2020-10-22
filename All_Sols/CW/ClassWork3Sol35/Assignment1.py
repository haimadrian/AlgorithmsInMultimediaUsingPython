__author__ = 'Dmitry Patashov'

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img4.jpeg')

plt.figure('RGB')
plt.imshow(img)

cv2.imshow('BGR', img)

plt.show()
cv2.waitKey()
