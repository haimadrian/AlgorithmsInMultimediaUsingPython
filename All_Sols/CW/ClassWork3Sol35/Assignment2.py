__author__ = 'Dmitry Patashov'

from PIL import Image
import cv2
from matplotlib import pyplot as plt

A = Image.open('img1.jpg')


if A.mode == 'RGB' or A.mode == 'BGR':
    img = cv2.imread('img2.jpg')
    b,g,r = cv2.split(img)

    plt.figure()
    plt.subplot(131)
    plt.title('R')
    plt.imshow(r, cmap='gray')
    plt.subplot(132)
    plt.title('G')
    plt.imshow(g, cmap='gray')
    plt.subplot(133)
    plt.title('B')
    plt.imshow(b, cmap='gray')
    plt.show()
