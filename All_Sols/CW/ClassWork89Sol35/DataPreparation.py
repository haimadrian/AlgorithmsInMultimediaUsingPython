__author__ = 'Dmitry Patashov'

import os
import cv2
import numpy as np

def LoadImageList():
    CurDir = os.getcwd()
    DataDir = CurDir + '\\Data\\' + 's'
    FileType = '.pgm'

    ImageList = list()
    for i in range(1,41):
        subList = []
        subDataDir = DataDir + str(i) + '\\'
        for j in range(1,11):
            FilePath = subDataDir + str(j) + FileType
            subList.append(cv2.imread(FilePath, 0))
        ImageList.append(subList)
    return ImageList

def ReconstructData(ImageList, Labels=40):
    m,n = ImageList[0][0].shape
    SampleSize = m*n

    TrainData = np.zeros([Labels * 5, SampleSize])
    TrainLabels = np.zeros([Labels * 5, 1])
    TestData = np.zeros([Labels * 3, SampleSize])
    TestLabels = np.zeros([Labels * 3, 1])
    ValidationData = np.float64(np.zeros([Labels * 2, SampleSize]))
    ValidationLabels = np.zeros([Labels * 2, 1])

    for i in range(Labels):
        for j in range(10):
            if j < 5:
                TrainData[5*i+j][:] = np.reshape(np.float64(ImageList[i][j]),[1,SampleSize])
                TrainLabels[5*i+j][0] = i
            elif j < 8:
                TestData[3*i+j-5][:] = np.reshape(np.float64(ImageList[i][j]),[1,SampleSize])
                TestLabels[3*i+j-5][0] = i
            elif j < 10:
                ValidationData[2*i+j-8][:] = np.reshape(np.float64(ImageList[i][j]),[1,SampleSize])
                ValidationLabels[2*i+j-8][0] = i
            else:
                raise ValueError('Image List doesnt match requirements')

    return TrainData, TrainLabels, TestData, TestLabels, ValidationData, ValidationLabels

def IsThisStringANumber(myStr):
    x = str(myStr)

    flag = x.replace('.','',1).replace('-','',1).isdigit()
    if x.replace('-','',1) != x and x[0] != '-':
        flag = False

    return flag
