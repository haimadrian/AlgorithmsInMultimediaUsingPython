__author__ = 'Dmitry Patashov'

import numpy as np

def myKMeans(k, Data):

    dataL = np.zeros((Data.shape[0], Data.shape[1]+1), dtype=np.float64)
    dataL[:,1:] = Data

    randInd = np.random.randint(0, Data.shape[0], k, np.int64)

    centroids = Data[randInd, :]
    labelsC = np.asarray(range(k))
    flag = 1
    while flag:
        for i in range(dataL.shape[0]):

            distVec = np.sum((centroids - dataL[i,1:]) ** 2, axis=1) ** 0.5

            dataL[i,0] = labelsC[np.argmin(distVec)]

        outL = 1
        newCentroids = np.zeros(centroids.shape)
        for j in range(k):

            if len(dataL[dataL[:, 0] == j, 0]):
                newCentroids[j,:] = np.mean(dataL[dataL[:,0] == j, :], axis=0)[1:]
            else:

                meanCent = np.mean(centroids, axis=0)

                if outL:
                    cenDistVec = np.sum((dataL[:, 1:] - meanCent) ** 2, axis=1) ** 0.5
                    newCentroids[j, :] = dataL[np.argmax(cenDistVec), 1:]
                    outL = 0
                else:
                    newCentroids[j, :] = meanCent
                    outL = 1


        if (newCentroids == centroids).all():
            flag = 0
        else:
            centroids = newCentroids

    return dataL

