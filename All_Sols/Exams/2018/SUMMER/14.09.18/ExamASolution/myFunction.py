__author__ = 'Dmitry Patashov'

import numpy as np
import numbers
import cv2
from matplotlib import pyplot as plt

def myCrossMatrix(n):

    I = np.eye(n)
    ir = I[:,::-1]
    myMat = I + ir
    if n % 2:
        ind = np.int64(np.floor(n/2.0))
        myMat[ind,ind] = 1

    return myMat

def myListMedian(myList):

    if myList.__class__ != [].__class__:
        return None

    return np.median(np.asarray([[x for x in myList if isinstance(x, numbers.Number)]]))

def myDictConst(myKey, MyVal):

    if myKey.__class__ != [].__class__ or \
            MyVal.__class__ != [].__class__ or \
            len(MyVal) != len(myKey):
        return None

    return {myKey[k]: MyVal[k] for k in range(len(MyVal))}

def myListEdit(myList, val, ch=0):

    if myList.__class__ != [].__class__:
        return None

    if ch:
        myList = myList + [val]
    else:
        myList.append(val)

    return myList

def myColorReplacement(img, read, write, amount):
    myImg = img.copy()
    # ------------------------------------------------------------------
    # for m in range(read, read + amount):
    #     for n in range(myImg.shape[1]):
    #         if myImg[m,n,0] < 10 or myImg[m,n,2] < 10:
    #             myImg[m - read + write, n, 1] = 255
    # ------------------------------------------------------------------
    myImg[write:write + amount,:, 1][np.logical_or(myImg[read:read + amount,:,0] < 10, myImg[read:read + amount,:,2] < 10)] = 255
    return myImg

def myMedianFilt(img, filtOrder=1):

    if img.__class__ != np.ndarray:
        return None

    if filtOrder.__class__ != np.int64:
        filtOrder = np.int64(filtOrder)

    if filtOrder < 0:
        filtOrder = 1

    D = img.shape
    if len(D) != 2:
        return None

    newImage = img.copy()

    borderSize = filtOrder
    PadImg = cv2.copyMakeBorder(img, filtOrder, filtOrder, filtOrder, filtOrder, cv2.BORDER_REPLICATE)
    m, n = PadImg.shape

    for i in range(borderSize, m - borderSize):
        for j in range(borderSize, n - borderSize):
            window = PadImg[i - borderSize:borderSize + i + 1, j - borderSize:borderSize + j + 1]
            med = np.median(window)
            newImage[i - borderSize, j - borderSize] = med

    return newImage

def myPolarGradient(img):

    im = np.float64(img.copy())
    SobelX = np.array([[-3, 0, 3],
                      [-10, 0, 10],
                      [-3, 0, 3]], dtype=np.float64)
    SobelY = SobelX.transpose()

    Gx = cv2.filter2D(im, -1, SobelX)
    Gy = cv2.filter2D(im, -1, SobelY)

    return (Gx**2 + Gy**2)**0.5, np.arctan2(Gy, Gx)

def myHistEq(Img):

    HistL = np.zeros(256)
    for i in range(256):
        HistL[i] = len(Img[Img == np.float64(i)])

    PDFfun = HistL / np.sum(HistL)

    CDFfun = np.zeros(PDFfun.shape)
    CDFfun[0] = PDFfun[0]
    for k in range(1, len(CDFfun)):
        CDFfun[k] = CDFfun[k - 1] + PDFfun[k]

    RepImg = np.float64(Img)
    for j in range(256):
        RepImg[RepImg == j] = CDFfun[j] * 255

    return np.uint8(np.round(RepImg))

def myPlotShape(im):

    r = 11
    plt.figure()
    plt.subplot(9, 11, 6 + 0 * r)
    plt.imshow(im)
    plt.axis('off')

    plt.subplot(9, 11, 5 + 1 * r)
    plt.imshow(im)
    plt.axis('off')
    plt.subplot(9, 11, 7 + 1 * r)
    plt.imshow(im)
    plt.axis('off')

    for k in range(1, 12):
        plt.subplot(9, 11, k + 2 * r)
        plt.imshow(im)
        plt.axis('off')

    plt.subplot(9, 11, 2 + 3 * r)
    plt.imshow(im)
    plt.axis('off')
    plt.subplot(9, 11, 4 + 3 * r)
    plt.imshow(im)
    plt.axis('off')
    plt.subplot(9, 11, 8 + 3 * r)
    plt.imshow(im)
    plt.axis('off')
    plt.subplot(9, 11, 10 + 3 * r)
    plt.imshow(im)
    plt.axis('off')

    plt.subplot(9, 11, 3 + 4 * r)
    plt.imshow(im)
    plt.axis('off')
    plt.subplot(9, 11, 9 + 4 * r)
    plt.imshow(im)
    plt.axis('off')

    plt.subplot(9, 11, 2 + 5 * r)
    plt.imshow(im)
    plt.axis('off')
    plt.subplot(9, 11, 4 + 5 * r)
    plt.imshow(im)
    plt.axis('off')
    plt.subplot(9, 11, 8 + 5 * r)
    plt.imshow(im)
    plt.axis('off')
    plt.subplot(9, 11, 10 + 5 * r)
    plt.imshow(im)
    plt.axis('off')

    for k in range(1, 12):
        plt.subplot(9, 11, k + 6 * r)
        plt.imshow(im)
        plt.axis('off')

    plt.subplot(9, 11, 5 + 7 * r)
    plt.imshow(im)
    plt.axis('off')
    plt.subplot(9, 11, 7 + 7 * r)
    plt.imshow(im)
    plt.axis('off')

    plt.subplot(9, 11, 6 + 8 * r)
    plt.imshow(im)
    plt.axis('off')

    plt.show()











