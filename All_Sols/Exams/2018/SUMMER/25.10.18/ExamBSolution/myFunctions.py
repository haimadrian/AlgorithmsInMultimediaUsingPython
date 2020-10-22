__author__ = 'Dmitry Patashov'

import numpy as np
import cv2
from matplotlib import pyplot as plt

def myPerimiterMatrix(n):
    if n != np.int64(n):
        return None

    myOne = np.ones((n, n))
    myOne[1:n-1, 1:n-1] = np.zeros((n - 2, n - 2)) * np.ones((n, n))[1:n-1, 1:n-1]

    return myOne

def countMyWords(myStr):

    if myStr.__class__ != ''.__class__:
        return None

    dis = ord('A') - ord('a')
    myL = list(myStr)
    for k in range(len(myL)):
        if ord(myL[k]) >= ord('A') and ord(myL[k]) <= ord('Z'):
            myL[k] = chr(ord(myL[k]) - dis)

    nL = ''.join(myL).split()
    myD = {}
    while len(nL):
        myD[nL[0]] = nL.count(nL[0])
        nL = filter(lambda a: a != nL[0], nL)

    return myD

def myListSum(myList):

    if myList.__class__ != [].__class__:
        return None

    mySum = 0
    for k in range(len(myList)):
        if myList[k].__class__ == [].__class__:
            mySum += myListSum(myList[k])
        else:
            mySum += myList[k]

    return mySum

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

def myKNNClasification(k, Data, L, Sam):

    if k != np.int64(k) or Data.__class__ != np.ndarray or Sam.__class__ != np.ndarray:
        return None

    Dist = np.sqrt(np.sum((Data - Sam)**2, 1))
    nni = np.argsort(Dist)[:k]

    rL = list(L[nni,:])
    ccV = []
    ccA = []
    while len(rL):
        ccA.append(rL.count(rL[0]))
        ccV.append(rL[0])
        rL = filter(lambda a : a != rL[0], rL)

    return ccV[np.argmax(ccA)]

def myPolarGradient(img):

    if img.__class__ != np.ndarray:
        return None

    im = np.float64(img.copy())
    SobelX = np.array([[-5,  0,  5],
                       [-13, 0, 13],
                       [-5,  0,  5]], dtype=np.float64)
    SobelY = SobelX.transpose()

    Gx = cv2.filter2D(im, -1, SobelX)
    Gy = cv2.filter2D(im, -1, SobelY)

    pMat = np.arctan2(Gy, Gx)
    pMat[pMat < 0] += 2 * np.pi

    return (Gx**2 + Gy**2)**0.5, pMat

def myPhaseRound(myMat):

    if myMat.__class__ != np.ndarray:
        return None

    myMat[np.logical_or(myMat <= 22.5, myMat > 157.5)] = 0
    myMat[np.logical_and(myMat > 22.5, myMat <= 67.5)] = 45
    myMat[np.logical_and(myMat > 67.5, myMat <= 112.5)] = 90
    myMat[np.logical_and(myMat > 112.5, myMat <= 157.5)] = 135

    return  myMat

def myPlotShape(img):

    if img.__class__ != np.ndarray:
        return None

    plt.figure()
    for k in range(1,225 + 1,2):
        plt.subplot(15,15,k)
        plt.imshow(img)
        plt.axis('off')
    plt.show()
















































