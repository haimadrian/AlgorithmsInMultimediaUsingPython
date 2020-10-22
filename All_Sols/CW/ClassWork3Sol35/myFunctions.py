__author__ = 'Dmitry Patashov'

import numpy as np
import cv2

# Assignment 3:
def myBGR2RGB(myImage):

    if myImage.__class__ == np.ndarray and len(myImage.shape) == 3:

        return myImage[:,:,::-1]
    else:
        return None

# Assignment 5:
def myGreenLine(myImage, linehalfSize = 50):

    if myImage.__class__ == np.ndarray:

        Dim = myImage.shape
        if len(Dim) == 2:

            imCenter = np.int(np.round(Dim[0]/2.0))
            if imCenter - linehalfSize <= 0 or imCenter + linehalfSize >= Dim[0]:
                linehalfSize = np.int(np.round(Dim[0]/10.0))

            newImageL = myImage.copy()
            newImageL[imCenter - linehalfSize: imCenter + linehalfSize,:] = 0
            myImage[imCenter - linehalfSize: imCenter + linehalfSize,:] = 255
            return cv2.merge((newImageL,myImage,newImageL))
        elif len(Dim) == 3:

            imCenter = np.int(np.round(Dim[0] / 2.0))
            if imCenter - linehalfSize <= 0 or imCenter + linehalfSize >= Dim[0]:
                linehalfSize = np.int(np.round(Dim[0] / 10.0))

            myImage[imCenter - linehalfSize: imCenter + linehalfSize,:,::2] = 0
            myImage[imCenter - linehalfSize: imCenter + linehalfSize, :, 1] = 255
            return myImage
        else:
            return None
    else:
        return None

# Assignment 6:
def myRedLine(myImage, linehalfSize = 25, cmap='BGR'):

    if myImage.__class__ == np.ndarray:

        if cmap == 'BGR':

            Dim = myImage.shape
            if len(Dim) == 3:

                its = min([Dim[0],Dim[1]])
                if its <= linehalfSize * 2 + 1:
                    linehalfSize = np.int(np.round(its/10.0))

                myDiag = np.eye(its)
                for i in range(1,linehalfSize):
                    myDiag += np.eye(its, k=i)
                    myDiag += np.eye(its, k=-i)
                myDiag = np.int64(myDiag)
                myNDiag = 1 - myDiag

                myImage = np.int64(myImage)
                myImage[:its, :its, 0] = myImage[:its, :its, 0] * myNDiag
                myImage[:its, :its, 1] = myImage[:its, :its, 1] * myNDiag
                myImage[:its, :its, 2] = myImage[:its, :its, 2] * myNDiag + myDiag * 255

                return np.uint8(myImage)

            elif len(Dim) == 2:
                return myRedLine(cv2.merge((myImage,myImage,myImage)), linehalfSize)
            else:
                return None

        elif cmap == 'RGB':
            return myRedLine(myImage[:,:,::-1], linehalfSize)
        else:
            raise ValueError('Not supported color map')
    else:
        return  None

# Assignment 7:
def myBlueSquare(myImage, halfSize = 10, cmap ='BGR'):

    if myImage.__class__ == np.ndarray:

        if cmap == 'BGR':

            Dim = myImage.shape
            if len(Dim) == 3:

                if halfSize * 2 + 1 > min([Dim[0],Dim[1]]):
                    halfSize = np.int(np.round(min([Dim[0],Dim[1]])/10.0))

                cy = np.int(np.round(Dim[0] / 2.0))
                cx = np.int(np.round(Dim[1] / 2.0))

                myImage[cy - halfSize: cy + halfSize, cx - halfSize: cx + halfSize, 0] = 255
                myImage[cy - halfSize: cy + halfSize, cx - halfSize: cx + halfSize, 1] = 0
                myImage[cy - halfSize: cy + halfSize, cx - halfSize: cx + halfSize, 2] = 0

                return myImage

            elif len(Dim) == 2:
                return myBlueSquare(cv2.merge((myImage, myImage, myImage)), halfSize)
            else:
                return None

        elif cmap == 'RGB':
            return myBlueSquare(myImage[:, :, ::-1], halfSize)
        else:
            raise ValueError('Not supported color map')
    else:
        return None

# Assignment 8:
def myPurpleCircle(myImage, Radius = 50):

    if myImage.__class__ == np.ndarray:

        Dim = myImage.shape
        if len(Dim) == 3:

            if Radius * 2 + 1 > min([Dim[0],Dim[1]]):
                halfSize = np.int(np.round(min([Dim[0],Dim[1]])/10.0))

            cy = np.int(np.round(Dim[0] / 2.0))
            cx = np.int(np.round(Dim[1] / 2.0))

            for i in range(Dim[0]):
                for j in range(Dim[1]):
                    if ((i-cy)**2 + (j-cx)**2)**0.5 <= Radius:

                        myImage[i,j, 0] = 150
                        myImage[i,j, 1] = 0
                        myImage[i,j, 2] = 150

            return myImage

        elif len(Dim) == 2:
            return myPurpleCircle(cv2.merge((myImage, myImage, myImage)), Radius)
        else:
            return None
    else:
        return None

# Assignment 9:
def myColorfullTriangle(myImage):

    if myImage.__class__ == np.ndarray:

        Dim = myImage.shape
        if len(Dim) == 3:

            size = np.int(np.round(min([Dim[0], Dim[1]]) / 5.0))
            lw = np.int(np.round(size / 2.0))
            cy = np.int(np.round(Dim[0] / 2.0))
            cx = np.int(np.round(Dim[1] / 2.0))

            Tc = (cy - size, cx)
            Lc = (np.int(np.round(cy - 1/3 * size)), np.int(np.round(cx - 8**0.5 / 3 * size)))
            Rc = (np.int(np.round(cy - 1/3 * size)), np.int(np.round(cx + 8**0.5 / 3 * size)))

            cv2.line(myImage, Tc[::-1], Lc[::-1], (255, 0, 0), lw)
            cv2.line(myImage, Tc[::-1], Rc[::-1], (0, 0, 255), lw)
            cv2.line(myImage, Rc[::-1], Lc[::-1], (0, 255, 0), lw)

            cv2.circle(myImage, Tc[::-1], np.int(np.round(lw / 2 + 1)), (255, 0, 255), -1)
            cv2.circle(myImage, Lc[::-1], np.int(np.round(lw / 2 + 1)), (255, 255, 0), -1)
            cv2.circle(myImage, Rc[::-1], np.int(np.round(lw / 2 + 1)), (0, 255, 255), -1)

            return myImage

        elif len(Dim) == 2:
            return myColorfullTriangle(cv2.merge((myImage, myImage, myImage)))
        else:
            return None
    else:
        return None

# Assignment 11:
def myZeroPadding(myImage, padSize=1):

    if myImage.__class__ == np.ndarray:

        Dim = myImage.shape
        if len(Dim) == 2:

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

# Assignment 12:
def myExtendedPadding(myImage, padSize=1):
    if myImage.__class__ == np.ndarray:

        Dim = myImage.shape
        if len(Dim) == 2:

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

# Assignment 13:
def GradientEdgeDetector(myImage, gradSensitivity = 1):

    if myImage.__class__ == np.ndarray:

        Dim = myImage.shape
        if len(Dim) == 2:

            # newImg = myExtendedPadding(myImage)
            dy, dx = np.gradient(np.float64(myImage))

            if gradSensitivity:
                newImg = (dy ** 2 + dx ** 2) ** 0.5
            else:
                newImg = np.abs((dy + dx) / 2.0)

            newImg = newImg - np.min(newImg)
            newImg = np.round(newImg * 255 / np.max(newImg))

            return np.uint8(newImg)

        elif len(Dim) == 3:

            b, g, r = cv2.split(myImage)
            Pb = GradientEdgeDetector(b)
            Pg = GradientEdgeDetector(g)
            Pr = GradientEdgeDetector(r)

            return cv2.merge((Pb, Pg, Pr))
        else:
            return None
    else:
        return None
