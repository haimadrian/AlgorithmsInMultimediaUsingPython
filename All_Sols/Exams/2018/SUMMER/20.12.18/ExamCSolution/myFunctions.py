__author__ = 'Dmitry Patashov'

import numpy as np
import cv2
from matplotlib import pyplot as plt
from numpy import linalg as LA

# Question 1
def myDashMatrix(n):

    if n != np.int64(n):
        return None

    myOne = np.zeros((n, n))
    myOne[:,::2] = 1

    return myOne

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

# Question 4
def myListEdit(myList, val, ch=0):

    if myList.__class__ != [].__class__:
        return None

    if ch:
        myList = myList + [val]
    else:
        myList.append(val)

    return myList

# Question 5
def TwoLiner(img):
    if img.__class__ != np.ndarray:
        return None

    im = img.copy()
    D = im.shape
    th = np.int64(np.round(D[0] / 3.))
    wi = np.int64(np.round(D[0] / 30.))
    if len(D) != 3 or D[0] < 30:
        return None

    # ----------------------------------------------------------
    # for m in range(th - wi, th + wi + 1):
    #     for n in range(D[1]):
    #         im[m, n, 0] = 150
    #         im[m, n, 1] = 255
    #         im[m, n, 2] = 0
    # for m in range(2*th - wi, 2*th + wi + 1):
    #     for n in range(D[1]):
    #         im[m, n, 0] = 150
    #         im[m, n, 1] = 255
    #         im[m, n, 2] = 0
    # ----------------------------------------------------------

    im[range(th - wi, th + wi + 1) + range(2 * th - wi, 2 * th + wi + 1), :, :] = np.array([150, 255, 0])

    return im

# Question 6
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

# Question 7
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

# Question 8
def myHalfEdgeMaskKernel(img):

    if img.__class__ != np.ndarray:
        return None

    newImg = np.float64(img.copy())
    maskX = np.array([[1, 0, -1],
                      [2, 0, -2],
                      [1, 0, -1]], dtype=np.float64)
    maskY = maskX.transpose()

    Xres = cv2.filter2D(newImg, -1, maskX)
    Yres = cv2.filter2D(newImg, -1, maskY)

    Rres = np.sqrt(Xres ** 2 + Yres ** 2)
    Rres = Rres - np.min(Rres[::2,:,:])
    Rres = 255 * Rres / np.max(Rres[::2,:,:])

    newImg[::2,:,:] = Rres[::2,:,:]
    newImg = np.uint8(np.round(newImg))

    return newImg

# Question 9
def myPlotShape(img):

    if img.__class__ != np.ndarray:
        return None

    plt.figure()
    for k in range(1,225 + 1,4):
        plt.subplot(15,15,k)
        plt.imshow(img)
        plt.axis('off')
    plt.show()
















































