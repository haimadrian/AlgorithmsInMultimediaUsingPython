__author__ = "Dmitry Patashov"

import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from numpy import linalg as LA


### Binary Logistic Regression ###
# List Filets
def list_files(directory):
    if os.path.exists(directory) == False:
        return None

    return [x for x in os.listdir(directory) if os.path.isfile(os.path.join(directory, x))]


# Load Files
def LoadImageData(dPath, fileNames):
    if os.path.exists(dPath) == False or fileNames.__class__ != [].__class__:
        return None

    Images = list()
    Labels = list()
    for f in fileNames:
        filePath = dPath + '/' + f
        Images.append(cv2.imread(filePath, 0))
        if f[-5].isdigit():
            Labels.append(np.float64(f[-5]))
        else:
            raise ValueError('The file name does not end with digit.')

    return Images, Labels


# Data Reconstruction
def ReconstructData(Images, Labels):
    if Labels.__class__ != [].__class__ or Images.__class__ != [].__class__:
        return None

    m, n = Images[0].shape
    k = len(Images)
    DataMat = np.zeros((k, m * n))
    LabelVec = np.array(Labels).reshape((-1, 1))

    for i in range(k):
        DataMat[i] = Images[i].reshape((1, -1))

    return DataMat, LabelVec


# Prepare Data
def LoadMnistData():
    dataPath = os.getcwd() + '/Data'
    testPath = dataPath + '/test'
    trainPath = dataPath + '/train'

    TestFileNames = list_files(testPath)
    TrainFileNames = list_files(trainPath)

    TestList, TestLabelList = LoadImageData(testPath, TestFileNames)
    TrainList, TrainLabelList = LoadImageData(trainPath, TrainFileNames)

    TestDataMat, TestLabelVec = ReconstructData(TestList, TestLabelList)
    TrainDataMat, TrainLabelVec = ReconstructData(TrainList, TrainLabelList)

    return TrainDataMat, TrainLabelVec, TestDataMat, TestLabelVec


# Create Binary Data
def BinarizeData(TrainDataMat, TrainLabelVec, TestDataMat, TestLabelVec, num1, num2):
    indListTr = list()
    for k in range(len(TrainLabelVec)):

        if TrainLabelVec[k] == num1:

            indListTr.append(k)
            TrainLabelVec[k] = 0.

        elif TrainLabelVec[k] == num2:

            indListTr.append(k)
            TrainLabelVec[k] = 1.

    indListTe = list()
    for k in range(len(TestLabelVec)):

        if TestLabelVec[k] == num1:

            indListTe.append(k)
            TestLabelVec[k] = 0.

        elif TestLabelVec[k] == num2:

            indListTe.append(k)
            TestLabelVec[k] = 1.

    return TrainDataMat[indListTr, :], TrainLabelVec[indListTr, :], TestDataMat[indListTe, :], TestLabelVec[indListTe, :]


# Regression Process #
# x is TrainData and w is the m*n independent variables. The result is a value between 0 to 1.
def SigmoidF(w, x):
    # 1 / ( 1 + e^(-z) )
    return 1 / (1 + np.exp(-x.dot(w)))


def myLogisticRegression(TrainData, TrainLabel, eps=0.01, sensitivity=10 ** (-7)):
    # Array with shape (TrainData.shape[1], 1) of random numbers between zero and maximum value in TrainData
    # That means we have m*n random values (independent variables)
    w0 = np.random.uniform(0, np.max(TrainData), (TrainData.shape[1], 1))

    data_ = TrainLabel - SigmoidF(w0, TrainData)
    dl0 = TrainData.transpose().dot(data_)

    w1 = w0 + eps * dl0
    dl1 = TrainData.transpose().dot(TrainLabel - SigmoidF(w1, TrainData))

    df = dl1 - dl0
    NormVal = LA.norm(df, 2) ** 2

    while NormVal > sensitivity:
        w0 = w1
        dl0 = dl1

        w1 = w0 + eps * dl0
        dl1 = TrainData.transpose().dot(TrainLabel - SigmoidF(w1, TrainData))

        df = dl1 - dl0
        NormVal = LA.norm(df, 2) ** 2

    return w1


def myLogisticClassification(TestData, w):
    appLabel = SigmoidF(w, TestData)
    appLabel[appLabel >= 0.5] = 1
    appLabel[appLabel < 0.5] = 0

    LabelVec = 1 - appLabel.reshape((-1, 1))

    return LabelVec


TrainDataMat, TrainLabelVec, TestDataMat, TestLabelVec = LoadMnistData()

num1, num2 = 0., 1.
bTrainDataMat, bTrainLabelVec, bTestDataMat, bTestLabelVec = BinarizeData(TrainDataMat, TrainLabelVec, TestDataMat, TestLabelVec, num1,
                                                                          num2)

W = myLogisticRegression(bTrainDataMat, bTrainLabelVec)

ApproximateLabel = myLogisticClassification(bTestDataMat, W)

acc = 100 * np.sum(np.abs(ApproximateLabel - bTestLabelVec)) / len(bTestLabelVec)

print(acc)
