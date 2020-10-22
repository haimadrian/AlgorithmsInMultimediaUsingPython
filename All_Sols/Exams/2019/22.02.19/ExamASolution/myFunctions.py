__author__ = 'Dmitry Patashov'

import numpy as np
import cv2
import os
from matplotlib import pyplot as plt
from numpy import linalg as LA

# Question 1
def myPlusMatrix(n):

    if n != np.int64(n):
        return None

    size = 2*n + 1
    myMat = np.zeros((size,size))
    myMat[n,:] = 1
    myMat[:,n] = 1

    return myMat

# Question 2
def countMyStrings(myStr):

    if myStr.__class__ != ''.__class__:
        return None

    dis = ord('A') - ord('a')
    myL = list(myStr)
    for k in range(len(myL)):
        if ord(myL[k]) >= ord('A') and ord(myL[k]) <= ord('Z'):
            myL[k] = chr(ord(myL[k]) - dis)

    myStrL = ''.join(myL)
    nL = myStrL.split()
    nL = list(set(nL))

    myD = {}
    for k in range(len(nL)):
        myD[nL[k]] = myStrL.count(nL[k])

    return myD

# Question 3
def myListMean(myList):

    if myList.__class__ != [].__class__:
        return None

    def myListMeanRec(myList):

        mySum = 0
        myAm = 0
        for k in range(len(myList)):
            if myList[k].__class__ == [].__class__:
                pSum , pAm = myListMeanRec(myList[k])
                mySum += pSum
                myAm += pAm
            else:
                mySum += myList[k]
                myAm += 1

        return mySum, myAm

    mySum, myAm = myListMeanRec(myList)

    myMean = mySum / myAm

    return myMean

# Question 4
def UpFolderConatin():

    currDir = os.getcwd()

    pathParts = currDir.split('\\')
    L = len(pathParts[-1])
    upDirr = currDir[:len(currDir)-L-1]

    ListItems = os.listdir(upDirr)

    return ListItems

# Question 5
def TwoLiner(img):
    if img.__class__ != np.ndarray:
        return None

    im = img.copy()
    D = im.shape
    th = np.int64(np.round(D[1] / 5.))
    wi = np.int64(np.round(D[1] / 30.))
    if len(D) != 3 or D[0] < 30:
        return None

    # ----------------------------------------------------------
    # for m in range(th - wi, th + wi + 1):
    #     for n in range(D[0]):
    #         im[n, m, 0] = 150
    #         im[n, m, 1] = 255
    #         im[n, m, 2] = 0
    # for m in range(4*th - wi, 4*th + wi + 1):
    #     for n in range(D[0]):
    #         im[n, m, 0] = 150
    #         im[n, m, 1] = 255
    #         im[n, m, 2] = 0
    # ----------------------------------------------------------

    im[:,range(th - wi, th + wi + 1) + range(4 * th - wi, 4 * th + wi + 1), :] = np.array([150, 255, 0])

    return im

# Question 6
def myLinearDependancyRemoval(DataMat):

    if DataMat.__class__ != np.ndarray:
        return None

    myData = np.float64(DataMat.copy())

    dataMean = np.mean(myData, axis=0)
    cData = myData - dataMean

    CovMat = cData.transpose().dot(cData)
    eigenVals, eigenVecMatU = LA.eigh(CovMat)

    V = eigenVecMatU[:, eigenVals > 10**(-9)]

    return myData.dot(V)

# Question 7
def myGradDescent(signal, time, startLoc, iterNum, stepSize):

    if signal.__class__ != np.ndarray or time.__class__ != np.ndarray:
        return None
    if iterNum != np.int64(iterNum):
        return None

    xn = startLoc
    indX = np.argmin(np.abs(time - xn))
    df = np.gradient(signal)

    for k in range(iterNum):
        xn = xn - stepSize * df[indX]
        indX = np.argmin(np.abs(time - xn))

    return xn



# Question 8
def mySignalFiltering(signal, order, T):

    if signal.__class__ != np.ndarray:
        return None
    if order != np.int64(order):
        return None
    if T != 0 and T != 1:
        return None

    pSig = np.concatenate((np.ones(order)*signal[1], signal, np.ones(order)*signal[-1]))
    fSig = np.zeros(signal.shape)
    for k in range(len(signal)):
        if T:
            fSig[k] = np.median(pSig[k:k + 2*order + 1])
        else:
            fSig[k] = np.mean(pSig[k:k + 2 * order + 1])

    return fSig

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





