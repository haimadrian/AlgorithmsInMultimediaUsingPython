__author__ = 'Alon Ziv'

import numpy as np, numbers, os, cv2, matplotlib.pyplot as plt


# Ex. 1
def myIdentityMatrix(n):
    if not isinstance(n, int) or n <= 0:
        return
    return np.identity(n, dtype=int)


# Ex. 2
def myArrayMean(list):
    if not isinstance(list, type([])):
        return
    nums = [value for value in list if isinstance(value, numbers.Number)]
    return np.mean(nums)


# Ex. 3
def myKNearest(k, x, myArray):
    if not isinstance(k, int) or k < 0\
            or not isinstance(x, float) \
            or not isinstance(myArray, np.ndarray) \
            or k > len(myArray)\
            or len([value for value in myArray if not isinstance(value, np.float64)]) > 0:
        return
    if k == len(myArray):
        return myArray
    dist = np.abs(myArray - x)
    # sol 1
    # kn = np.ndarray(k)
    # for i in range(k):
    #     idx_min = np.argmini(dist)
    #     kn[i] = myArray[idx_min]
    #     dist[idx_min] = np.max(dist)
    # sol 2
    kn = myArray[np.argpartition(dist, k)[:k]]
    return kn


# Ex. 4
def myDirLongName():
    dir = os.getcwd()
    files = [filename for filename in os.listdir(dir) if os.path.isfile(os.path.join(dir, filename))]
    return files[np.argmax([len(file) for file in files])]


# Ex. 5
def myFastToneReplacement(img, fromA, toB, equalsC):
    myImg = img.copy()
    myImg[np.logical_and(myImg >= fromA, myImg <= toB)] = equalsC
    return myImg

# Ex. 6
def myMedianFilt(img, filtOrder):
    if not isinstance(img, np.ndarray) or not isinstance(filtOrder, int) or filtOrder < 1:
        return
    shape = img.shape
    newImg = np.ndarray(shape)
    paddedImg = cv2.copyMakeBorder(img, filtOrder, filtOrder, filtOrder,filtOrder, cv2.BORDER_CONSTANT, 0)
    window = 2 * filtOrder + 1
    for i in range(shape[0]):
        for j in range(shape[1]):
            newImg[i, j] = np.median(paddedImg[i:i + 1 + window, j:j + 1 + window])
    return newImg


# Ex. 7
def myPhaseRound(myMat):
    first, last, step = 0, 180, 45
    if not isinstance(myMat, np.ndarray) or len([value for value in myMat.reshape((myMat.size, 1)) if value < first or value > last]) > 0:
        return
    steps = range(first, last + 1, step)
    for value in steps:
        low = steps[0] if value == steps[0] else value - step // 2 - 1
        high = steps[-1] if value == steps[-1] else value + step // 2
        myMat = myFastToneReplacement(myMat, low, high, value % last)
    return myMat


# Ex. 8
def myHistEq(img):
    if not isinstance(img, np.ndarray):
        return
    HistL = np.zeros(256)
    for i in range(256):
        HistL[i] = len(img[img == i])
    PDFfun = HistL / np.sum(HistL)
    CDFfun = np.zeros(PDFfun.shape)
    CDFfun[0] = PDFfun[0]
    for k in range(1, len(CDFfun)):
        CDFfun[k] = CDFfun[k - 1] + PDFfun[k]
    newImg = np.float64(img)
    for j in range(256):
        newImg[newImg == j] = CDFfun[j] * 255
    return np.uint8(np.round(newImg))

# Ex. 9
def myPlotShape(img):
    if not isinstance(img, np.ndarray):
        return
    border = np.ones((np.int64(img.shape[0] * 0.15), img.shape[1])) * 255
    img = np.concatenate((border, img, border))
    plt.figure()
    plt.subplot(141)
    plt.axis('off')
    plt.imshow(img, cmap='gray')
    plt.subplot(142)
    plt.axis('off')
    img2 = np.concatenate((border, border, img, border, border))
    plt.imshow(np.concatenate((img2, img2)), cmap='gray')
    white = np.ones(img.shape) * 255
    plt.subplot(143)
    plt.axis('off')
    plt.imshow(np.concatenate((img, white, white, img)), cmap='gray')
    plt.subplot(144)
    plt.axis('off')
    plt.imshow(np.concatenate((img, img, img, img, img)), cmap='gray')
    plt.show()
