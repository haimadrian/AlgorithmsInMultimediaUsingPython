__author__ = 'Dmitry Patashov'

import numpy as np
import cv2

def GaussBlur(Image):

    img = np.float64(Image.copy())
    D = len(img.shape)
    if D == 2:

        GausMask = (1.0 / 273) * np.array([[1,  4,  7,  4, 1],
                                           [4, 16, 26, 16, 4],
                                           [7, 26, 41, 26, 7],
                                           [4, 16, 26, 16, 4],
                                           [1,  4,  7,  4, 1]],
                                          dtype=np.float64)

        return cv2.filter2D(img, -1,  GausMask)

    elif D == 3:

        b,g,r = cv2.split(img)
        Gb = GaussBlur(b)
        Gg = GaussBlur(g)
        Gr = GaussBlur(r)

        return cv2.merge((Gb,Gg,Gr))

    else:
        raise ValueError('Function receives only BGR, RGB or GrayScale images')

def SobelMasking(Image):

    img = np.float64(Image.copy())
    D = len(img.shape)
    if D == 2:

        SobelMaskX = np.array([[-1, 0, 1],
                               [-2, 0, 2],
                               [-1, 0, 1]],
                              dtype=np.float64)

        SobelMaskY = np.array([[ 1,  2,  1],
                               [ 0,  0,  0],
                               [-1, -2, -1]],
                              dtype=np.float64)

        SobelImgX = cv2.filter2D(img, -1, SobelMaskX)
        SobelImgY = cv2.filter2D(img, -1, SobelMaskY)

        return SobelImgX, SobelImgY
    elif D == 3:

        b,g,r = cv2.split(img)
        SbX, SbY = SobelMasking(b)
        SgX, SgY = SobelMasking(g)
        SrX, SrY = SobelMasking(r)

        SobelImg3X = np.dstack((SbX, SgX, SrX))
        SobelImg3Y = np.dstack((SbY, SgY, SrY))

        return SobelImg3X, SobelImg3Y
    else:
        raise ValueError('Function receives only BGR, RGB or GrayScale images')

def PhaseMatrixCalculation(GradientX, GradientY):

    D = (len(GradientX.shape) + len(GradientY.shape))/2
    if D == 2:

        return np.arctan2(GradientY, GradientX)

    elif D == 3:

        bgx, ggx, rgx = cv2.split(GradientX)
        bgy, ggy, rgy = cv2.split(GradientY)

        pmb = PhaseMatrixCalculation(bgx, bgy)
        pmg = PhaseMatrixCalculation(ggx, ggy)
        pmr = PhaseMatrixCalculation(rgx, rgy)

        return cv2.merge((pmb, pmg, pmr))
    else:
        raise ValueError('Function receives only BGR, RGB or GrayScale images and both input matrices must be of identical shape')

def NonMaximumSuppressionStep1(PhaseMat):

    myPhaseMat = PhaseMat.copy()
    D = len(myPhaseMat.shape)
    if D == 2:

        myPhaseMat[myPhaseMat < 0] += np.pi
        myPhaseMat *= 180 / np.pi

        myPhaseMat[myPhaseMat <= 22.5] = 0
        myPhaseMat[np.logical_and(myPhaseMat > 22.5, myPhaseMat <= 67.5)] = 45
        myPhaseMat[np.logical_and(myPhaseMat > 67.5, myPhaseMat <= 112.5)] = 90
        myPhaseMat[np.logical_and(myPhaseMat > 112.5, myPhaseMat <= 157.5)] = 135
        myPhaseMat[myPhaseMat > 157.5] = 0

        return myPhaseMat

    elif D == 3:
        pmb, pmg, pmr = cv2.split(myPhaseMat)

        nmsb = NonMaximumSuppressionStep1(pmb)
        nmsg = NonMaximumSuppressionStep1(pmg)
        nmsr = NonMaximumSuppressionStep1(pmr)

        return cv2.merge((nmsb, nmsg, nmsr))
    else:
        raise ValueError('Function receives only BGR, RGB or GrayScale images')

def NonMaximumSuppressionStep2(IntansityGradient, PhaseMat):

    D = (len(PhaseMat.shape) + len(IntansityGradient.shape)) / 2
    if D == 2:

        m,n = IntansityGradient.shape
        Mat = np.zeros((m+2,n+2))
        Mat[1:m+1, 1:n+1] = IntansityGradient

        SuppressedGradient = np.zeros((m,n))

        for i in range(1,m+1):
            for j in range(1,n+1):
                if PhaseMat[i-1,j-1] == 0:
                    # north and south
                    if np.max(Mat[i, j-1:j+2:2]) >= np.max(Mat[i-1:i+2:2, j]):
                        SuppressedGradient[i-1, j-1] = IntansityGradient[i - 1, j - 1]

                elif PhaseMat[i-1,j-1] == 45:
                    # north west and south east
                    if np.max((Mat[i-1, j-1], Mat[i+1, j+1])) >= np.max((Mat[i-1,j+1], Mat[i+1,j-1])):
                        SuppressedGradient[i - 1, j - 1] = IntansityGradient[i - 1, j - 1]

                elif PhaseMat[i-1,j-1] == 90:
                    # east and west
                    if np.max(Mat[i-1:i+2:2, j]) >= np.max(Mat[i, j-1:j+2:2]):
                        SuppressedGradient[i - 1, j - 1] = IntansityGradient[i - 1, j - 1]

                elif PhaseMat[i-1,j-1] == 135:
                    # north east and south west
                    if np.max((Mat[i+1,j-1], Mat[i-1,j+1])) >= np.max((Mat[i-1,j-1], Mat[i+1,j+1])):
                        SuppressedGradient[i - 1, j - 1] = IntansityGradient[i - 1, j - 1]

                else:
                    raise ValueError('Phase logic encountered critical error')

        return SuppressedGradient
    elif D == 3:
        pmb, pmg, pmr = cv2.split(PhaseMat)
        igb, igg, igr = cv2.split(IntansityGradient)

        nmsb = NonMaximumSuppressionStep2(igb, pmb)
        nmsg = NonMaximumSuppressionStep2(igg, pmg)
        nmsr = NonMaximumSuppressionStep2(igr, pmr)

        return cv2.merge((nmsb, nmsg, nmsr))
    else:
        raise ValueError('Function receives only BGR, RGB or GrayScale images and both input matrices must be of identical shape')

def DoubleThresholding(IntansityGradient, lowT, highT):

    myIntansityGradient = IntansityGradient.copy()

    D = len(myIntansityGradient.shape)
    if D == 2:

        ths = np.array((lowT, highT), dtype=np.float64)
        ths[ths < 0] = 0
        ths[ths > 1] = 1
        ths = np.sort(ths)

        lowT = ths[0]
        highT = ths[1]

        myIntansityGradient = myIntansityGradient - np.min(myIntansityGradient)
        myIntansityGradient = myIntansityGradient / np.max(myIntansityGradient)

        EdgeMap = np.zeros(myIntansityGradient.shape, dtype=np.float64)

        EdgeMap[myIntansityGradient >= highT] = 2
        EdgeMap[np.logical_and(myIntansityGradient >= lowT, myIntansityGradient < highT)] = 1

        return EdgeMap


    elif D == 3:
        igb, igg, igr = cv2.split(myIntansityGradient)

        dtb = DoubleThresholding(igb, lowT, highT)
        dtg = DoubleThresholding(igg, lowT, highT)
        dtr = DoubleThresholding(igr, lowT, highT)

        return cv2.merge((dtb, dtg, dtr))
    else:
        raise ValueError('Function receives only BGR, RGB or GrayScale images')

def TrackEdgesByHysteresis(EdgeMap):

    D = len(EdgeMap.shape)
    if D == 2:

        m,n = EdgeMap.shape
        edgeMap = np.zeros((m+2,n+2), dtype=np.float64)
        edgeMap[1:m+1, 1:n+1] = EdgeMap.copy()

        locs = np.where(edgeMap == 2)
        tmp = list(zip(list(locs[0]), list(locs[1])))
        myStack = list(tmp)

        flag = len(myStack)

        while flag:

            row, col = myStack.pop()
            flag = len(myStack)

            subMat = edgeMap[row-1:row+1, col-1:col+1]
            locs = list(np.where(subMat == 1))
            locs[0] += row-1
            locs[1] += col-1
            locs = tuple(locs)

            edgeMap[locs] = 2

            tmp = list(zip(list(locs[0]), list(locs[1])))
            coor = list(tmp)
            myStack += coor

        edgeMap = edgeMap[1:m + 1, 1:n + 1]
        edgeMap[edgeMap == 1] = 0
        edgeMap /= 2

        return edgeMap

    elif D == 3:

        b, g, r = cv2.split(EdgeMap)
        Eb = TrackEdgesByHysteresis(b)
        Eg = TrackEdgesByHysteresis(g)
        Er = TrackEdgesByHysteresis(r)

        return cv2.merge((Eb, Eg, Er))

    else:
        raise ValueError('Function receives only BGR, RGB or GrayScale images')
