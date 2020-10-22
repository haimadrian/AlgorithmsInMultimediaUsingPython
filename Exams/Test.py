__author__ = "Haim Adrian"

from matplotlib import pyplot as plt
import numpy as np
import cv2
from numbers import Number


# 1
def mmyMaskKernel(img, maskKernel):
    if img.__class__ != np.ndarray or maskKernel.__class__ != np.ndarray:
        return None
    return cv2.filter2D(img, -1, maskKernel)


# original
def myMaskKernel(img, maskKernel):
    if img.__class__ != np.ndarray or maskKernel.__class__ != np.ndarray:
        return
    img = np.float64(img)
    maskKernel = np.float64(maskKernel)
    shape = img.shape
    windowy = maskKernel.shape[0]
    windowx = maskKernel.shape[1]
    y = (windowy - 1) // 2
    x = (windowx - 1) // 2
    newImg = np.zeros((shape[0] - (windowy - 1), (shape[1] - (windowx - 1))), dtype=np.float64)
    imgPadded = np.float64(cv2.copyMakeBorder(img, y, y, x, x, cv2.BORDER_CONSTANT, 0))
    for i in range(y, shape[0] - y):
        for j in range(x, shape[1] - x):
            subMat = np.float64(imgPadded[i - y:i + y + 1, j - x:j + x + 1])
            newImg[i - y, j - x] = np.sum(subMat * np.float64(maskKernel))
    return newImg


def myMasking(myImage, myMask):
    Dim = myImage.shape
    a, b = myMask.shape
    m, n = Dim[0], Dim[1]

    if m < a or n < b or a % 2 == 0 or np.mod(b, 2) == 0:
        return None

    p = np.int64(m)
    q = np.int64(n)
    LRBorders = np.int64((b - 1) / 2)
    UDBorders = np.int64((a - 1) / 2)

    imgPadded = np.float64(cv2.copyMakeBorder(myImage, UDBorders, UDBorders, LRBorders, LRBorders, cv2.BORDER_CONSTANT, 0))
    Result = np.zeros((p, q))
    for i in range(UDBorders, m - UDBorders):
        for j in range(LRBorders, n - LRBorders):
            subMat = np.float64(imgPadded[i - UDBorders:i + UDBorders + 1, j - LRBorders:j + LRBorders + 1])
            Result[i - UDBorders, j - LRBorders] = np.sum(subMat * np.float64(myMask))

    return Result


# ex8
img = cv2.imread('eagle.jpeg', 0)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
SharpenMask = np.array([[-1, -2, -1],
                        [-2, 13, -2],
                        [-1, -2, -1]], dtype=np.float64)
GausMask = (1.0 / 273) * np.array([[1, 4, 7, 4, 1],
                                   [4, 16, 26, 16, 4],
                                   [7, 26, 41, 26, 7],
                                   [4, 16, 26, 16, 4],
                                   [1, 4, 7, 4, 1]],
                                  dtype=np.float64)
my_sol = mmyMaskKernel(img, SharpenMask)
print(np.min(my_sol), np.max(my_sol))
my_sol = np.uint8((my_sol - np.min(my_sol)) / np.max(my_sol) * 255)
masked = myMaskKernel(img, SharpenMask)
masked = np.uint8((masked - np.min(masked)) / np.max(masked) * 255)
third = myMasking(img, SharpenMask)
print(np.min(third), np.max(third))
third = np.uint8((third - np.min(third)) / np.max(third) * 255)
plt.subplot(131)
plt.imshow(masked, CMAP='gray')
plt.subplot(132)
plt.imshow(my_sol, CMAP='gray')
plt.subplot(133)
plt.imshow(third, CMAP='gray')
plt.show()
