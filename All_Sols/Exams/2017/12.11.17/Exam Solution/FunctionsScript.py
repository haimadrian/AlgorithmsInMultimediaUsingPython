__author__ = 'Dmitry Patashov'

import numpy as np
import os
import cv2
from matplotlib import pyplot as plt

def myFullTensor(myDim):

    if myDim.__class__ == tuple:
        return np.ones(myDim) * 7.5
    else:
        return None

def myFilesList(myFolder=None):

    if myFolder == None or not(os.path.exists(myFolder)):
        myFolder = os.getcwd()

    contentList = os.listdir(myFolder)

    fileList = [x for x in contentList if os.path.isfile(os.path.join(myFolder, x))]

    return fileList

def myImageMean(img):

    if img.__class__ != np.ndarray:
        return None
    else:
        return np.mean(np.float64(img))

def myCommonTone(img):

    if img.__class__ != np.ndarray:
        return None
    else:
        myHist = np.zeros(256)
        for i in range(256):
            myHist[i] = len(img[img == i])

        return np.argmax(myHist)

def myLine(img):

    myImg = img.copy()
    center = myImg.shape[0] // 2
    # ------------------------------------------------------------------
    myImg[center - 30: center + 40, ::, 2] =0
    # ------------------------------------------------------------------
    return myImg

def myPhaseRound(myMat):

    if myMat.__class__ != np.ndarray:
        return None
    else:

        myMat[np.logical_or(myMat <= 22.5, myMat > 157.5)] = 0
        myMat[np.logical_and(myMat > 22.5, myMat <= 67.5)] = 45
        myMat[np.logical_and(myMat > 67.5, myMat <= 112.5)] = 90
        myMat[np.logical_and(myMat > 112.5, myMat <= 157.5)] = 135

        return  myMat

def myDataSplit(FullData):

    if FullData.__class__ != np.ndarray:
        return None
    else:

        TrData = FullData[0:5,::]
        TeData = FullData[5:7,::]
        ValData = FullData[7:10,::]

        for i in range(1,10):

            TrData = np.concatenate((TrData, FullData[10 * i:10 * i + 5, ::]), axis=0)
            TeData = np.concatenate((TeData, FullData[10 * i + 5:10 * i + 7, ::]), axis=0)
            ValData = np.concatenate((ValData, FullData[10 * i + 7:10 * i + 10, ::]), axis=0)

        return TrData, TeData, ValData

def myFunctionPlotter(funName):

    if funName.__class__ != ''.__class__:
        return None
    elif funName not in ['sin', 'cos', 'con', 'All']:
        return None
    else:

        x = np.linspace(0, 2*np.pi,1000)

        plt.figure()

        def myPlotCreator(funName, x):

            if funName == 'sin':
                y = np.sin(x)
                plt.plot(x,y, 'b')
            elif funName == 'cos':
                y = np.cos(x)
                plt.plot(x, y, 'g')
            elif funName == 'con':
                y = x * 0
                plt.plot(x, y, 'r')
            elif funName == 'All':
                myPlotCreator('sin', x)
                myPlotCreator('cos', x)
                myPlotCreator('con', x)

        myPlotCreator(funName, x)
        plt.show()

def myPlotShape(img):

    if img.__class__ != np.ndarray:
        return None
    else:

        plt.figure()

        plt.subplot(1,4,1)
        plt.axis('off')
        plt.imshow(img, cmap='gray')

        plt.subplot(2,4,2)
        plt.axis('off')
        plt.imshow(img, cmap='gray')

        plt.subplot(2,4,6)
        plt.axis('off')
        plt.imshow(img, cmap='gray')

        plt.subplot(4,4,3)
        plt.axis('off')
        plt.imshow(img, cmap='gray')

        plt.subplot(4,4,15)
        plt.axis('off')
        plt.imshow(img, cmap='gray')

        plt.subplot(5,4,4)
        plt.axis('off')
        plt.imshow(img, cmap='gray')

        plt.subplot(5,4,8)
        plt.axis('off')
        plt.imshow(img, cmap='gray')

        plt.subplot(5,4,12)
        plt.axis('off')
        plt.imshow(img, cmap='gray')

        plt.subplot(5,4,16)
        plt.axis('off')
        plt.imshow(img, cmap='gray')

        plt.subplot(5,4,20)
        plt.axis('off')
        plt.imshow(img, cmap='gray')

        plt.show()