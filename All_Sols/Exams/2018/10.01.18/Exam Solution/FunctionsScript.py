__author__ = 'Dmitry Patashov'

import numpy as np
import numbers
import os
import cv2
from matplotlib import pyplot as plt

def myIdentityMatrix(n):


    if n != np.round(n):
        return None
    elif n <= 0:
        return None

    return np.eye(n)

def myArrayMean(myList):

    if myList.__class__ != [].__class__:
        return None

    numList = []
    for Instance in myList:
        tst = isinstance(Instance, numbers.Number)
        if tst:
            numList.append(Instance)

    return np.mean(np.asarray(numList))

def myKNearest(k, x, myArray):

    if k != np.round(k):
        return None
    elif k <= 0:
        return None

    if myArray.__class__ != np.ndarray:
        return None
    a=np.abs(x-myArray)
    a = np.argsort(a)
    return myArray[a[0:k]]
    # indArr = np.argsort(np.abs(x - myArray))
    # return np.sort(myArray[indArr[0:k]])

def myDirLongName():

    cwd = os.getcwd()
    mylist=os.listdir(cwd)
    filelist = [x for x in mylist if os.path.isfile(cwd+'//'+x)]
    a=len(filelist)
    b=np.zeros(a)
    for i in range(a):
        b[i]=len(filelist[i])
    return filelist[np.argmax(b)]


    # fileList = [x for x in os.listdir(cwd) if os.path.isfile(cwd + '//' + x)]
    # items = len(fileList)
    # lenArr = np.zeros(items)
    #
    # for i in range(items):
    #     lenArr[i] = len(fileList[i])

    # return fileList[np.argmax(lenArr)]

def myFastToneReplacement(img, fromA, toB, equalsC):

    myImg = img.copy()
    myImg[:,:,:][np.logical_and(myImg>=fromA, myImg<=toB)] =equalsC
    return myImg

def myMedianFilt(img, filtOrder=1):

    if img.__class__ != np.ndarray:
        return None

    if filtOrder.__class__ != np.int64:
        filtOrder = np.int64(filtOrder)

    if filtOrder < 0:
        filtOrder = 1

    D = img.shape
    if len(D) == 2:

        newImage = np.zeros(D)

        borderSize = filtOrder
        PadImg = cv2.copyMakeBorder(img, filtOrder, filtOrder, filtOrder, filtOrder, cv2.BORDER_REPLICATE)
        m, n = PadImg.shape

        for i in range(borderSize, m - borderSize):
            for j in range(borderSize, n - borderSize):
                window = PadImg[i - borderSize:borderSize + i + 1, j - borderSize:borderSize + j + 1]
                med = np.median(window)
                newImage[i - borderSize, j - borderSize] = med

        return newImage

    else:
        return None

def myPhaseRound(myMat):

    if myMat.__class__ != np.ndarray:
        return None
    else:

        myMat[np.logical_or(myMat <= 22.5, myMat > 157.5)] = 0
        myMat[np.logical_and(myMat > 22.5, myMat <= 67.5)] = 45
        myMat[np.logical_and(myMat > 67.5, myMat <= 112.5)] = 90
        myMat[np.logical_and(myMat > 112.5, myMat <= 157.5)] = 135

        return  myMat

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
    # for j in range(256):
    #     RepImg[RepImg == j] = CDFfun[j] * 255

    return np.uint8(np.round(RepImg))

def myPlotShape(img):

    if img.__class__ != np.ndarray:
        return None
    else:

        plt.figure()

        plt.subplot(1,4,1)
        plt.axis('off')
        plt.imshow(img, cmap='gray')

        plt.subplot(1,3,2)
        plt.axis('off')
        plt.imshow(img, cmap='gray')
        #
        # plt.subplot(2,4,6)
        # plt.axis('off')
        # plt.imshow(img, cmap='gray')
        #
        # plt.subplot(4,4,3)
        # plt.axis('off')
        # plt.imshow(img, cmap='gray')
        #
        # plt.subplot(4,4,15)
        # plt.axis('off')
        # plt.imshow(img, cmap='gray')
        #
        # plt.subplot(5,4,4)
        # plt.axis('off')
        # plt.imshow(img, cmap='gray')
        #
        # plt.subplot(5,4,8)
        # plt.axis('off')
        # plt.imshow(img, cmap='gray')
        #
        # plt.subplot(5,4,12)
        # plt.axis('off')
        # plt.imshow(img, cmap='gray')
        #
        # plt.subplot(5,4,16)
        # plt.axis('off')
        # plt.imshow(img, cmap='gray')
        #
        # plt.subplot(5,4,20)
        # plt.axis('off')
        # plt.imshow(img, cmap='gray')

        plt.show()