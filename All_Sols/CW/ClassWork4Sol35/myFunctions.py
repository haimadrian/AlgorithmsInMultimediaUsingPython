__author__ = 'Dmitry Patashov'

import numpy as np
import cv2
import logicFunctions as lf

def myMasking(myImage, myMask):
    if myImage.__class__ == np.ndarray and myMask.__class__ == np.ndarray:

        Dim = myImage.shape
        if len(Dim) == 2:
            a, b = myMask.shape
            m, n = Dim[0], Dim[1]

            if m < a or n < b or a % 2 == 0 or np.mod(b, 2) == 0:
                return None

            p = np.int64(m - (a - 1))
            q = np.int64(n - (b - 1))
            LRBorders = np.int64((b - 1) / 2)
            UDBorders = np.int64((a - 1) / 2)

            Result = np.zeros((p, q))
            for i in range(UDBorders, m - UDBorders):
                for j in range(LRBorders, n - LRBorders):
                    subMat = np.float64(myImage[i - UDBorders:i + UDBorders + 1, j - LRBorders:j + LRBorders + 1])
                    Result[i - UDBorders, j - LRBorders] = np.sum(subMat * np.float64(myMask))

            return Result

        elif len(Dim) == 3:

            b, g, r = cv2.split(myImage)
            Mb = myMasking(b, myMask)
            Mg = myMasking(g, myMask)
            Mr = myMasking(r, myMask)

            if Mb.__class__ == None.__class__ or Mg.__class__ == None.__class__ or Mr.__class__ == None.__class__:
                return None

            return cv2.merge((Mb, Mg, Mr))
        else:
            return None

    else:
        return None

def myHistPlotUint8(myImage):

    if myImage.__class__ != np.ndarray:
        return None


    Dim = myImage.shape
    if len(Dim) == 2:
        if myImage[0,0].__class__ != np.uint8:
            return None

        maxVal = np.max(myImage)
        minVal = np.min(myImage)
        Result = np.zeros(256, dtype=np.int64)

        for k in range(maxVal - minVal + 1):
            Result[k + minVal] = len(myImage[myImage == k + minVal])

        return Result
    else:
        return None
