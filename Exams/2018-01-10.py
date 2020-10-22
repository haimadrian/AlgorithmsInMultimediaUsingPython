__author__ = "Haim Adrian"

import matplotlib
import numpy as np
import os
from numbers import Number


def myIdentity(n):
    identity = np.zeros((n, n))
    np.fill_diagonal(identity, 1)
    return identity


def myIdentityLoop(n):
    identity = np.zeros((n, n))
    for i in range(n):
        identity[i, i] = 1
    return identity


def myArrayMean(lst):
    theCount = 0
    theSum = 0
    for i in lst:
        if isinstance(i, Number):
            theSum += i
            theCount += 1
    return theSum / theCount


def myKNearest(k, x, arr):
    return arr[np.argsort(np.abs(arr - x))[:k]]


def myDirLongName():
    files = [f for f in os.listdir(os.getcwd()) if os.path.isfile(f)]
    print(max(files, key=len))


def myFastToneReplacementLoop(img, fromA, toB, equalsC):
    myImg = img.copy()

    D = myImg.shape
    if len(D) == 2:
        for i in range(D[0]):
            for j in range(D[1]):
                if myImg[i, j] >= fromA and myImg[i, j] <= toB:
                    myImg[i, j] = equalsC
    elif len(D) == 3:
        for m in range(D[0]):
            for n in range(D[1]):
                for k in range(D[2]):
                    if myImg[m, n, k] >= fromA and myImg[m, n, k] <= toB:
                        myImg[m, n, k] = equalsC
    else:
        return None

    return myImg


def myFastToneReplacement(img, fromA, toB, equalsC):
    myImg = img.copy()
    myImg[np.logical_and(myImg >= fromA, myImg <= toB)] = equalsC
    return myImg


# ones = np.ones((5, 5))
# ones[1:4, 1:4] *= 4
# print(myFastToneReplacementLoop(ones, 3, 6, 0))
# print(myFastToneReplacement(ones, 3, 6, 0))
result = myKNearest(3, -1.2, np.array([-3.2, 8, 1, 0, -1.1, 0.1, 12]))
print(result)
