# 305265514
__author__ = "Haim Adrian"

import numpy as np
import operator


def MostCommonColor(myImage):
    if not isinstance(myImage, np.ndarray):
        return None

    if myImage.ndim == 2:
        # For 2D image just count each scalar and return the maximum one
        unique, counts = np.unique(myImage, return_counts=True)
        return unique[np.argmax(counts)]
    elif myImage.ndim == 3:
        # Define a dictionary to count the occurrences of each color in the specified image
        countsDic = {}

        # Scan the whole matrix of colors, instead of sub-calling MostCommonColor, cause we need to count colors
        # and not finding the maximum scalar in each level of z.
        for row in range(myImage.shape[0]):
            for col in range(myImage.shape[1]):
                # Make current color a tuple so we can register it as key in a dictionary
                currColor = (myImage[row, col, 0], myImage[row, col, 1], myImage[row, col, 2])
                countsDic[currColor] = countsDic.get(currColor, 0) + 1

        # Return the key where its value is the maximum one among all values in the dictionary
        return max(countsDic.items(), key=operator.itemgetter(1))[0]
    else:
        return None
