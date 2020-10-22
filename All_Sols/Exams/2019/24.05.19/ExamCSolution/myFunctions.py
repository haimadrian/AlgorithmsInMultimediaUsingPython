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
def myListHist(myList):

    if myList.__class__ != [].__class__:
        return None

    def myListSimplifier(myList, mySimpleList):

        for k in range(len(myList)):
            if myList[k].__class__ == [].__class__:
                myListSimplifier(myList[k], mySimpleList)
            else:
                mySimpleList.append(np.float64(myList[k]))

        return None

    mySimpleList = list()
    myListSimplifier(myList, mySimpleList)

    myValArr = np.asarray(mySimpleList)
    maxVal = np.int64(np.max(myValArr))
    myHist = np.zeros((maxVal + 1))

    for k in range(maxVal + 1):
        myHist[k] = len(myValArr[myValArr == k])

    return myHist


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
def myFastToneReplacement(img, fromA, toB, equalsC):
    if img.__class__ != np.ndarray:
        return None

    myImg = img.copy()
    # ------------------------------------------------------------------
    # D = myImg.shape
    # if len(D) == 2:
    #     for i in range(D[0]):
    #         for j in range(D[1]):
    #             if myImg[i, j] >= fromA and myImg[i, j] <= toB:
    #                 myImg[i, j] = equalsC
    # elif len(D) == 3:
    #     for m in range(D[0]):
    #         for n in range(D[1]):
    #             for k in range(D[2]):
    #                 if myImg[m, n, k] >= fromA and myImg[m, n, k] <= toB:
    #                     myImg[m, n, k] = equalsC
    # else:
    #     return None
    # ------------------------------------------------------------------

    myImg[np.logical_and(myImg>=fromA, myImg<=toB)] = equalsC

    return myImg


# Question 6
def myLRcycles(TrainData, TrainLabel, W, gamma, iterNum):

    if TrainData.__class__ != np.ndarray or TrainLabel.__class__ != np.ndarray or W.__class__ != np.ndarray:
        return None
    if iterNum != np.int64(iterNum) or gamma != np.abs(gamma):
        return None

    def SigmoidF(w, x):
        return 1 / (1 + np.exp(-x.dot(w)))

    def DerivativeCalcF(TrainData, TrainLabel, w):

        return TrainData.transpose().dot(TrainLabel - SigmoidF(w, TrainData))

    for k in range(iterNum):

        W = W + gamma * DerivativeCalcF(TrainData, TrainLabel, W)

    return W


# Question 7
def myGradDescent(signal, time, startLoc, iterNum, stepSize):

    if signal.__class__ != np.ndarray or time.__class__ != np.ndarray:
        return None
    if iterNum != np.int64(iterNum) or stepSize != np.abs(stepSize):
        return None

    xn = startLoc
    indX = np.argmin(np.abs(time - xn))
    df = np.gradient(signal)

    for k in range(iterNum):
        xn = xn - stepSize * df[indX]
        indX = np.argmin(np.abs(time - xn))

    return xn


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
def myPeakDetect(Signal):

    if Signal.__class__ != np.ndarray:
        return None

    locs = []
    for k in range(1,len(Signal)-1):

        if Signal[k] > Signal[k-1] and Signal[k] > Signal[k+1]:
            locs.append(k)

    return np.asarray(locs)


























