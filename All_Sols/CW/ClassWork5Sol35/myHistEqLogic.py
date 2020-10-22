__author__ = 'Dmitry Patashov'

import numpy as np

def myHistEqualization(Img):

    HistL = np.zeros(256)
    for i in range(256):
        HistL[i] = len(Img[Img == np.float64(i)])

    PDFfun = HistL / np.sum(HistL)

    CDFfun = np.zeros(PDFfun.shape)
    CDFfun[0] = PDFfun[0]
    for k in range(1, len(CDFfun)):
        CDFfun[k] = CDFfun[k - 1] + PDFfun[k]

    RepImg = np.float64(Img)
    for j in range(256):
        RepImg[RepImg == j] = CDFfun[j] * 255

    return np.uint8(np.round(RepImg))
