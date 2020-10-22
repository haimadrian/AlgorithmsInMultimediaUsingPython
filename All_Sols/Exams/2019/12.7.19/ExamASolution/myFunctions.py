__author__ = 'Dmitry Patashov'

import numpy as np
import cv2
import os
from matplotlib import pyplot as plt
from numpy import linalg as LA


# Question 1
def myChessMatrix(n):

    if n != np.uint64(n):
        return None

    size = 2*n
    myMat = np.zeros((size,size))
    myMat[0::2, 1::2] = 1
    myMat[1::2, 0::2] = 1

    return myMat


# Question 2
def countMyChars(myStr):

    if myStr.__class__ != ''.__class__:
        return None

    myLstr = myStr.lower()
    myD = {}
    while myLstr != '':
        myD[myLstr[0]] = myLstr.count(myLstr[0])
        myLstr = myLstr.replace(myLstr[0], '')

    return myD


# Question 3
def myListMax(myList, maxVal=None):

    if myList.__class__ != [].__class__:
        return None

    for k in range(len(myList)):
        if myList[k].__class__ == [].__class__:
            maxVal = myListMax(myList[k], maxVal)
        else:
            if maxVal == None:
                maxVal = np.float64(myList[k])
            elif maxVal < np.float64(myList[k]):
                maxVal = np.float64(myList[k])

    return maxVal


# Question 4
def myKNearest(k, x, myArray):

    if k != np.round(k):
        return None
    elif k <= 0:
        return None

    if myArray.__class__ != np.ndarray:
        return None

    indArr = np.argsort(np.abs(x - myArray))

    return myArray[indArr[0:k]]


# Question 5
def myColorShift(img):
    if img.__class__ != np.ndarray:
        return None

    im = img.copy()
    D = im.shape
    if len(D) != 3:
        return None

    # ----------------------------------------------------------
    # for m in range(D[0]):
    #     for n in range(D[1]):
    #         if im[m,n,0] > 200:
    #             im[m,n,1] = im[m,n,0]
    # ----------------------------------------------------------

    im[:,:,1][im[:,:,0] > 200] = im[:,:,0][im[:,:,0] > 200]

    return im


# Question 6
def mySignalFiltering(signal, order, T):

    if signal.__class__ != np.ndarray:
        return None
    if order != np.int64(order):
        return None
    if T != 0 and T != 1:
        return None

    pSig = np.concatenate((np.ones(order)*signal[0], signal, np.ones(order)*signal[-1]))
    fSig = np.zeros(signal.shape)
    for k in range(len(signal)):
        if T:
            fSig[k] = np.median(pSig[k:k + 2*order + 1])
        else:
            fSig[k] = np.mean(pSig[k:k + 2 * order + 1])

    return fSig


# Question 7
def myDiagEdgeDetect(image, rad):

    if image.__class__ != np.ndarray:
        return None
    if rad != np.int64(rad):
        return None

    D = image.shape
    if len(D) == 2:
        img = np.float64(image.copy())
        sobY = np.array([[1,   2,  1],
                         [0,   0,  0],
                         [-1, -2, -1]], dtype=np.float64)
        sobX = sobY.transpose()

        gx = cv2.filter2D(img, -1, sobX)
        gy = cv2.filter2D(img, -1, sobY)

        intGrad = np.sqrt(gx **2 + gy **2)

        binMap = np.tri(D[0], D[1], -rad) + (1 - np.tri(D[0], D[1], rad))

        DiagEdge = intGrad * (1 - binMap)
        imgNoDiag = img * binMap

        limVal = np.round(DiagEdge + imgNoDiag)
        limVal[limVal > 255] = 255
        im = np.uint8(limVal)

        return im
    else:

        b,g,r = cv2.split(image)

        B = myDiagEdgeDetect(b, rad)
        G = myDiagEdgeDetect(g, rad)
        R = myDiagEdgeDetect(r, rad)

        return cv2.merge((B,G,R))


# Question 8
def myKMeansIter(dataMet, centers):
    if type(dataMet) != np.ndarray or type(centers) != np.ndarray:
        return None
    if len(dataMet.shape) != 2 or len(centers.shape) != 2:
        return None

    dim = dataMet.shape
    labels = np.zeros((dim[0]))
    for i in range(dim[0]):
        labels[i] = np.argmin(np.sqrt(np.sum((centers - dataMet[i])**2, axis=1)))

    nCe = centers.copy()
    for i in range(nCe.shape[0]):
        a2 = labels == i
        a1 = dataMet[a2]
        nCe[i] = np.mean(a1, axis=0)
    return nCe


# Question 9
def myOddIndexSuppression1(img):

    myImg = img.copy()
    # ---------------------------------------------------------------------------
    # for m in range(img.shape[0]):
    #     for n in range(img.shape[1]):
    #         if not np.mod(m+n,2):
    #             myImg[m, n] = 0
    # ---------------------------------------------------------------------------
    myImg[0::2, 0::2], myImg[1::2, 1::2] = 0, 0

    return myImg

def myOddIndexSuppression2(img):

    myImg = img.copy()
    # ---------------------------------------------------------------------------
    # for m in range(img.shape[0]):
    #     for n in range(img.shape[1]):
    #         if not np.mod(m+n,2):
    #             myImg[m, n] = 0
    # ---------------------------------------------------------------------------
    myImg = myImg * np.mod(np.asarray(range(img.shape[1])) + np.reshape(np.asarray(range(img.shape[0])), (img.shape[0], 1)), 2)

    return myImg


























