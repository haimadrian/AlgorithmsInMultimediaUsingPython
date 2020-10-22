__author__ = 'Dmitry Patashov'

import cv2
from matplotlib import pyplot as plt

img4 = cv2.imread('img4.jpeg')

b,g,r = cv2.split(img4)
R = cv2.merge((r,g*0,b*0))
G = cv2.merge((r*0,g,b*0))
B = cv2.merge((r*0,g*0,b))

Bt = b.transpose()
Gu = g[::-1,:]

plt.figure()
plt.subplot(131)
plt.title('R')
plt.imshow(R)
plt.subplot(132)
plt.title('G')
plt.imshow(G)
plt.subplot(133)
plt.title('B')
plt.imshow(B)

plt.figure()
plt.imshow(cv2.merge((r,Gu,Bt)))

plt.show()
