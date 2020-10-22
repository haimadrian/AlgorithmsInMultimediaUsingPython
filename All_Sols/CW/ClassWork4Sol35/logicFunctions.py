__author__ = 'Dmitry Patashov'

import numpy as np
import cv2


def myZeroPadding(myImage, padSize=1):

    if myImage.__class__ == np.ndarray:

        Dim = myImage.shape
        if len(Dim) == 2:

            padSize = np.int64(padSize)
            m, n = Dim[0], Dim[1]
            NewImg = np.zeros([m + 2 * padSize, n + 2 * padSize])
            NewImg[padSize:m + padSize, padSize:n + padSize] = myImage

            return np.uint8(NewImg)

        elif len(Dim) == 3:

            b, g, r = cv2.split(myImage)
            Pb = myZeroPadding(b, padSize)
            Pg = myZeroPadding(g, padSize)
            Pr = myZeroPadding(r, padSize)

            return cv2.merge((Pb, Pg, Pr))
        else:
            return None
    else:
        return None

def myExtendedPadding(myImage, padSize=1):
    if myImage.__class__ == np.ndarray:

        Dim = myImage.shape
        if len(Dim) == 2:

            padSize = np.int64(padSize)
            newImg = myZeroPadding(myImage, padSize)

            def extendTopDown(newImg, padSize, dim):

                newImg[:padSize, :] = newImg[padSize, :]
                newImg[dim + padSize:, :] = newImg[dim + padSize - 1, :]

                return newImg

            newImg = extendTopDown(newImg, padSize, Dim[0])
            newImg = extendTopDown(newImg.transpose(), padSize, Dim[1]).transpose()

            return np.uint8(newImg)

        elif len(Dim) == 3:

            b, g, r = cv2.split(myImage)
            Pb = myExtendedPadding(b, padSize)
            Pg = myExtendedPadding(g, padSize)
            Pr = myExtendedPadding(r, padSize)

            return cv2.merge((Pb, Pg, Pr))
        else:
            return None
    else:
        return None

def MedianSQFilter(myImage, filtOrder=1):

    if myImage.__class__ != np.ndarray:
        return None

    D = myImage.shape
    if len(D) == 2:

        windowSize = filtOrder * 2 + 1

        if windowSize % 2 == 0:
            windowSize += 1
        if windowSize < 3 or windowSize > np.min(D):
            windowSize = 3

        newImage = np.zeros(D)

        borderSize = np.int64((windowSize - 1) / 2)
        PadImg = myExtendedPadding(myImage, borderSize)
        m,n = PadImg.shape

        for i in range(borderSize, m - borderSize):
            for j in range(borderSize, n - borderSize):
                window = PadImg[i-borderSize:borderSize+i+1, j-borderSize:borderSize+j+1]
                arr = np.reshape(window, (1,-1))
                Sarr = np.sort(arr)
                med = Sarr[0][np.int64((windowSize ** 2 - 1) / 2)]
                newImage[i-borderSize][j-borderSize] = med

        return newImage

    elif len(D) == 3:

        b,g,r = cv2.split(myImage)
        MB = MedianSQFilter(b, filtOrder)
        MG = MedianSQFilter(g, filtOrder)
        MR = MedianSQFilter(r, filtOrder)

        return cv2.merge((MB,MG,MR))
    else:
        raise ValueError('Function receives only BGR, RGB or GrayScale images')
