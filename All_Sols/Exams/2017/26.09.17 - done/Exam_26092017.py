__author__ = 'Alon Ziv'

import numpy as np, os, matplotlib.pyplot as plt, cv2


def myTensTnsor(dim):
    if dim.__class__ != ().__class__:
        return
    for item in dim:
        if type(item) != int or item < 0:
            return
    return np.ones(dim, dtype=int) * 10


def myFilesList(dir=os.getcwd()):
    if dir.__class__ != ''.__class__:
        return
    if os.path.exists(dir) == False:
        dir = os.getcwd()
    return [file for file in os.listdir(dir) if os.path.isfile(os.path.join(dir, file))]


def myImageMedian(img):
    if img.__class__ != np.ndarray:
        return
    return np.median(img)


def myImageNegative(img):
    if img.__class__ != np.ndarray:
        return
    return 255 - img


def myFastToneReplacement(img, fromA, toB, equalsC):
    myImg = img.copy()
    myImg[np.logical_and(myImg >= fromA, myImg <= toB)] = equalsC
    return myImg


def myRGBsplit(img):
    if img.__class__ != np.ndarray:
        return
    b, g, r = cv2.split(img)
    R = cv2.merge((r, g * 0, b * 0))
    G = cv2.merge((r * 0, g, b * 0))
    B = cv2.merge((r * 0, g * 0, b))
    plt.figure()
    plt.subplot(131)
    plt.title('R')
    plt.axis('off')
    plt.imshow(R)
    plt.subplot(132)
    plt.title('G')
    plt.axis('off')
    plt.imshow(G)
    plt.subplot(133)
    plt.title('B')
    plt.axis('off')
    plt.imshow(B)
    plt.show()


def myMedianFilt(img, filtOrder):
    if img.__class__ != np.ndarray or filtOrder.__class__ != int or filtOrder < 0:
        return
    shape = img.shape
    newImg = np.zeros(shape)
    imgPadded = cv2.copyMakeBorder(img, filtOrder, filtOrder, filtOrder, filtOrder, cv2.BORDER_CONSTANT, 0)
    window = 2 * filtOrder + 1
    for i in range(shape[0]):
        for j in range(shape[1]):
            newImg[i, j] = np.median(imgPadded[i:i + window, j:j + window])
    return newImg

def myMaskKernel(img, maskKernel):
    if img.__class__ != np.ndarray or maskKernel.__class__ != np.ndarray:
        return
    shape = img.shape
    newImg = np.zeros(shape)
    windowy = maskKernel.shape[0]
    windowx = maskKernel.shape[1]
    y = (windowy - 1) // 2
    x = (windowx - 1) // 2
    imgPadded = cv2.copyMakeBorder(img, y, y, x, x, cv2.BORDER_REPLICATE)
    for i in range(shape[0]):
        for j in range(shape[1]):
            newImg[i, j] = np.sum(imgPadded[i:i + windowy, j:j + windowx] * maskKernel)
    return newImg

def myPlotShape(img):
    if img.__class__ != np.ndarray:
        return
    border = np.ones((img.shape[0], np.int64(img.shape[1] * 0.1))) * 255
    img = np.concatenate((border, img, border), axis=1)
    plt.figure()
    plt.subplot(411)
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.subplot(412)
    plt.imshow(np.concatenate((img, img), axis=1), cmap='gray')
    plt.axis('off')
    plt.subplot(413)
    whiteSpace = np.ones(img.shape) * 255
    plt.imshow(np.concatenate((img, whiteSpace, whiteSpace, img), axis=1), cmap='gray')
    plt.axis('off')
    plt.subplot(414)
    plt.imshow(np.concatenate((img, img, img, img, img), axis=1), cmap='gray')
    plt.axis('off')
