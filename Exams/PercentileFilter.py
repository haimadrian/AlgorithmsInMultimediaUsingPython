# ID
__author__ = "Haim Adrian"

import numpy as np
import cv2
from numbers import Number


def PercentileFilter(myImage, order=1):
    if not isinstance(myImage, np.ndarray):
        return None

    if order is None or not isinstance(order, Number) or order <= 0:
        order = 1

    # Make sure order is an integer
    order = np.int64(order)

    dim = myImage.shape
    dimLen = len(dim)
    if dimLen == 2:
        # Use copy padding so we will keep the same image dimensions
        paddedImg = cv2.copyMakeBorder(myImage, order, order, order, order, cv2.BORDER_REPLICATE)
        padDim = paddedImg.shape
        newImg = np.zeros(myImage.shape)

        for i in range(order, padDim[0] - order):
            for j in range(order, padDim[1] - order):
                # Construct current window based on the specified order. (window is 2*order + 1)
                window = paddedImg[i - order:order + i + 1, j - order:order + j + 1]

                # Get the mean of current window
                windowMean = np.mean(window)

                # Use percentile to find the percentile based on current mean. Use np.round to match nearest integer and not floor
                per = np.percentile(window, int(np.round(100 * windowMean / 255)))
                newImg[i - order, j - order] = per

        return newImg
    elif dimLen == 3:
        b, g, r = cv2.split(myImage)
        b = PercentileFilter(b, order)
        g = PercentileFilter(g, order)
        r = PercentileFilter(r, order)

        return cv2.merge((b, g, r))
    else:
        return None
