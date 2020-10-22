__author__ = 'Dmitry Patashov'

import numpy as np
from matplotlib import pyplot as plt

def PlotData(Data, size=50, showGr = 1, newWin = 1, titleT = None):

    if newWin:
        plt.figure()

    if titleT != None:
        plt.title(titleT)

    plt.scatter(Data[:,1][Data[:,0]==0], Data[:,2][Data[:,0]==0], color='red', s=size)

    plt.scatter(Data[:,1][Data[:,0]==1], Data[:,2][Data[:,0]==1], color='green', s=size)

    plt.scatter(Data[:,1][Data[:,0]==2], Data[:,2][Data[:,0]==2], color='blue', s=size)

    if showGr:
        plt.show()

def myKNN(k, Data, NewSamples):

    if k < 1:
        k = 1
    elif k > Data.shape[0]:
        k = Data.shape[0]

    for i in range(NewSamples.shape[0]):

        distVec = np.sum((Data[:,1:] - NewSamples[i,1:]) ** 2, axis=1) ** 0.5
        sortInds = np.argsort(distVec)

        kNearest = sortInds[0:k]

        unique, counts = np.unique(Data[kNearest,0], return_counts=True)

        maxApp = np.max(counts)
        if len(counts[counts == maxApp]) > 1:

            labArr = unique[counts == maxApp].ravel()
            distToL = np.zeros(len(labArr))
            for j in range(len(labArr)):
                distToL[j] = np.sum(distVec[kNearest][Data[kNearest, 0] == labArr[j]])

            newLabel = labArr[np.argmin(distToL)]

        else:

            newLabel = unique[np.argmax(counts)]

        NewSamples[i, 0] = newLabel

    return NewSamples

