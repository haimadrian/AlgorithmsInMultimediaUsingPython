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

    size = 2*n
    myMat = np.zeros((size,size))
    myMat[n:,:n] = 1
    myMat[:n,n:] = 1

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
def myListMedian(myList):

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

    myMedian = np.median(np.array(mySimpleList))

    return myMedian


# Question 4
def UpFolderContain():

    currDir = os.getcwd()

    pathParts = currDir.split('\\')
    L = len(pathParts[-1])
    upDirr = currDir[:len(currDir)-L-1]

    ListItems = os.listdir(upDirr)

    return ListItems


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


# Question 9
def SaltAndPepperSignalNoise(Signal, NoisePr):

    if Signal.__class__ != np.ndarray:
        return None
    if NoisePr < 0 or NoisePr > 1:
        return None

    amm = np.int64(np.round(NoisePr * len(Signal)))
    inds = np.random.randint(0, len(Signal), amm)
    noise = np.random.normal(0, 0.5, amm)

    Signal[inds] += noise

    return Signal


