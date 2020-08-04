__author__ = "Haim Adrian"

import numpy as np
import cv2
from matplotlib import pyplot as plt


# Assignment 1
def normalizeImage(img):
    img = img - np.min(img)
    img = np.round(img * 255 / np.max(img))
    return np.uint8(img)


def myMasking(img, mask):
    if not isinstance(img, np.ndarray) or not isinstance(mask, np.ndarray):
        print("Not ndarray")
        return None

    maskShape = mask.shape
    imgShape = img.shape
    if (len(maskShape) != 2) or (maskShape[0] != maskShape[1]) or (maskShape[0] % 2 == 0):
        print("Mask is not supported. Only two square odd dimensional masks. e.g. 3x3 or 5x5")
        return None

    def myMaskingInner(img2D, msk):
        # Find the pad size. For example, we will get 1 in case dim is 3, or 2 in case dim is 5, and so on
        mid = np.int((msk.shape[0] - 1) / 2)

        # Extended padding
        padded = cv2.copyMakeBorder(img2D, mid, mid, mid, mid, cv2.BORDER_REPLICATE)
        result = np.float64(np.zeros(img2D.shape))

        # Now apply the mask
        for i in range(mid, padded.shape[0] - mid):
            for j in range(mid, padded.shape[1] - mid):
                result[i-mid, j-mid] = np.sum(padded[i-mid:i+mid+1, j-mid:j+mid+1] * msk)

        return result

    if len(imgShape) > 3 or len(imgShape) < 2:
        print("Illegal image dimension. Length of shape can be 2 or 3 only")
        return None

    if len(imgShape) == 2:
        return myMaskingInner(img, mask)

    b, g, r = cv2.split(img)
    return cv2.merge((myMaskingInner(b, mask), myMaskingInner(g, mask), myMaskingInner(r, mask)))


# Assignment 2
def someMask():
    img = cv2.imread("BlurryImage1.jpg")
    mask = np.array([[-1, -1, -1],
                     [-1, 10, -1],
                     [-1, -1, -1]])

    masked = normalizeImage(np.abs(myMasking(img, mask)))
    return img, masked


# Assignment 3
def myHistPlot(img1, img2):
    if not isinstance(img1, np.ndarray) or not isinstance(img2, np.ndarray):
        print("Not ndarray")
        return None

    if (len(img1.shape) != 2) or (len(img2.shape) != 2):
        print("Grayscale (2D) expected")
        return None

    def histogram(img):
        hist = {}

        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if img[i, j] in hist:
                    hist[img[i, j]] += 1
                else:
                    hist[img[i, j]] = 1

        return hist

    hist1 = histogram(img1)
    hist2 = histogram(img2)

    # when there is a big difference between max and min, we can barely understand anything from the plot, so set max.
    hist1Vals = [x if x <= 30000 else 30000 for x in hist1.values()]
    hist2Vals = [x if x <= 30000 else 30000 for x in hist2.values()]
    plt.figure('Plot images')
    plt.subplot(221)
    plt.bar(hist1.keys(), hist1Vals, color='b', fc='k', ec='k')
    plt.title('Image1 Hist')
    plt.subplot(222)
    plt.bar(hist2.keys(), hist2Vals, color='b', fc='k', ec='k')
    plt.title('Image2 Hist')
    plt.subplot(223)
    plt.imshow(img1[:, :], cmap="gray")
    plt.axis('off')
    plt.title('Image1')
    plt.subplot(224)
    plt.imshow(img2[:, :], cmap="gray")
    plt.axis('off')
    plt.title('Image2')
    plt.show()


# Assignment 4
def medianFilter():
    img = cv2.imread("NoisyS.pgm")

    def medianFilterInner(img2D):
        windowSize = 10 * 2 + 1

        # Find the pad size. For example, we will get 1 in case dim is 3, or 2 in case dim is 5, and so on
        mid = np.int((windowSize - 1) / 2)

        # Zero padding
        padded = cv2.copyMakeBorder(img2D, mid, mid, mid, mid, cv2.BORDER_CONSTANT, value=0)
        result = np.float64(np.zeros(img2D.shape))

        # Now apply the filter
        fullWindowLength = windowSize**2
        for i in range(mid, padded.shape[0] - mid):
            for j in range(mid, padded.shape[1] - mid):
                medianArray = np.reshape(padded[i-mid:i+mid+1, j-mid:j+mid+1], (1, fullWindowLength))
                result[i-mid, j-mid] = np.median(medianArray)

        return result

    b, g, r = cv2.split(img)
    medianB = medianFilterInner(b)
    medianG = medianFilterInner(g)
    medianR = medianFilterInner(r)

    gaussianMask = (1 / 273) * np.array([[1, 4, 7, 4, 1],
                                         [4, 16, 26, 16, 4],
                                         [7, 26, 41, 26, 7],
                                         [4, 16, 26, 16, 4],
                                         [1, 4, 7, 4, 1]])

    return img, cv2.merge((myMasking(medianB, gaussianMask), myMasking(medianG, gaussianMask), myMasking(medianR, gaussianMask)))


# Assignment 5
def drawRedDiagonalLine(img):
    if img is None:
        return None
    dim = img.shape

    x1, y1 = 0, 0
    x2, y2 = dim[1], dim[0]
    image = img.copy()

    line_thickness = 2
    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), thickness=line_thickness)

    return image
