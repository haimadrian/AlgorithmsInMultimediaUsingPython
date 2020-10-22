__author__ = 'Dmitry Patashov'

import numpy as np
import cv2
import os
from matplotlib import pyplot as plt
from numpy import linalg as LA


# Question 1
def myTriangularMatrix (n):

    if n != np.uint64(n):
        return None

    return 1 - np.tri(n,k=-1)


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
def myListMin(myList, minVal=None):

    if myList.__class__ != [].__class__:
        return None

    for k in range(len(myList)):
        if myList[k].__class__ == [].__class__:
            minVal = myListMin(myList[k], minVal)
        else:
            if minVal == None:
                minVal = np.float64(myList[k])
            elif minVal > np.float64(myList[k]):
                minVal = np.float64(myList[k])

    return minVal


# Question 4
def myFileSearch(myPath, myExtention):
    if myPath.__class__ != ''.__class__:
        return None
    elif myExtention.__class__ != ''.__class__:
        return None

    return [x for x in os.listdir(myPath)
            if (os.path.isfile(myPath + '//' + x) and x.endswith(myExtention))]


# Question 5
def myBorderCreation(img, borders):
    if img.__class__ != np.ndarray or np.int64(borders) != borders:
        return None

    im = img.copy()
    D = im.shape
    if len(D) != 3:
        return None

    # ----------------------------------------------------------
    # for n in range(D[1]):
    #     if n < borders or n - D[1] > (-1 - borders):
    #         im[:, n] = (np.mean(im[:,:,0]), np.mean(im[:,:,1]), np.mean(im[:,:,2]))
    # ----------------------------------------------------------

    im[:,range(borders) + range(-1,-borders-1,-1)] = (np.mean(im[:,:,0]), np.mean(im[:,:,1]), np.mean(im[:,:,2]))

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


# Question 8
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


























