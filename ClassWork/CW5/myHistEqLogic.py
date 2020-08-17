__author__ = "Haim Adrian"

import collections

import numpy as np
from matplotlib import pyplot as plt
import cv2


# Probability Density Function
# Result is a histogram containing weights (density) e.g. colorCount / sum(colorsCount)
def myPDF(tensor, p=8):
    if not isinstance(tensor, np.ndarray):
        print("PDF: Not a tensor. Was: ", tensor.__class__)
        return None

    tensorShape = tensor.shape
    if (len(tensorShape) > 3) or (len(tensorShape) < 2):
        print("PDF: Unexpected dimension. Was: ", tensorShape)
        return None

    pdf = np.zeros(2 ** p, dtype=np.float64)
    if len(tensor.shape) == 3:
        for i in range(tensorShape[0]):
            for j in range(tensorShape[1]):
                for k in range(tensorShape[2]):
                    pdf[int(tensor[i, j, k])] += 1
    else:
        for j in range(tensorShape[0]):
            for k in range(tensorShape[1]):
                pdf[int(tensor[j, k])] += 1

    # Now divide by the sum
    pdf /= pdf.sum()

    return pdf


# Cumulative Distribution Function
# p tells how many bits an image is, so we can scan the pdf accordingly. 2^p is the amount of elements in pdf
def myCDF(pdfTensor, p=8):
    if not isinstance(pdfTensor, collections.Sequence) and not (isinstance(pdfTensor, np.ndarray) and (len(pdfTensor.shape) == 1)):
        print("CDF: Not a sequence. Was:", pdfTensor.__class__)
        return None

    length = 2 ** p
    if len(pdfTensor) != length:
        print("CDF: PDF tensor should be a sequence with", length, "elements. Was:", len(pdfTensor))
        return None

    # Declare array of zeros with the same length of the pdf
    cdf = np.zeros(length, dtype=np.float64)
    cdf[0] = pdfTensor[0]
    for j in range(1, length):
        cdf[j] = cdf[j - 1] + pdfTensor[j]

    return cdf


def applyCDFFilter(img, cdf):
    if cdf is None:
        return None

    if not isinstance(img, np.ndarray) or not isinstance(cdf, np.ndarray):
        print("CDFFilter: Not a tensor. Was: Image=", img.__class__, ", CDF=", cdf.__class__)
        return None

    imgShape = img.shape
    if (len(imgShape) > 3) or (len(imgShape) < 2):
        print("CDFFilter: Unexpected dimension. Was: ", imgShape)
        return None

    def doFilter(twoDImg):
        shape = twoDImg.shape
        for j in range(shape[0]):
            for k in range(shape[1]):
                twoDImg[j, k] *= cdf[int(twoDImg[j, k])]
        return twoDImg

    if len(imgShape) == 3:
        b, g, r = cv2.split(img)
        return cv2.merge((doFilter(b), doFilter(g), doFilter(r)))
    else:
        return doFilter(img)


# Result is (hist, binEdges) where hist contains the weights (density) and binEdges contains the colors 0-255 inclusive
def numpyPDF(tensor, p=8):
    if not isinstance(tensor, np.ndarray):
        print("PDF: Not a tensor. Was:", tensor.__class__)
        return None

    size = 2 ** p + 1
    # range is 0 to 255 inclusive (2**p - 1)
    return np.histogram(tensor, range=range(size), bins=range(size), density=True)


def plot(title, img, location):
    plt.subplot(location)
    plt.imshow(np.uint8(img[:, :, ::-1]))
    plt.title(title)
    plt.axis('off')
    plt.xticks([])
    plt.yticks([])
