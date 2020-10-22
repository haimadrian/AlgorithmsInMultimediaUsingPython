__author__ = "Haim Adrian"

import matplotlib
import numpy as np
from numbers import Number


def myPlusMatrix(n):
    matt = np.zeros((2 * n + 1, 2 * n + 1), dtype=np.int8)
    matt[n, :] = 1
    matt[:, n] = 1
    return matt


def countMyStrings(string):
    lowercase = str(string).lower()
    words = lowercase.split(' ')
    stringsCount = {}
    while words:
        currWord = words[0]
        stringsCount[currWord] = lowercase.count(currWord)
        words = list(filter(lambda val: val != currWord, words))
    return stringsCount


def myListMean(lst):
    def flatList(lst_inner):
        flattened = []
        for item in lst_inner:
            if isinstance(item, Number):
                flattened += [item]
            elif isinstance(item, list):
                flattened += flatList(item)
        return flattened

    allNumbers = flatList(lst)
    print('Flattened list:', allNumbers)
    return sum(allNumbers) / len(allNumbers)


# result = myListMean([1, [2], 3, [1, -1, [2, 3, [1.0], 1], 2], -3, 1.0, [[0]]])
# print(result)
def myOddIndexSuppressionLoop(img):
    myImg = img.copy()
    for m in range(img.shape[0]):
        for n in range(img.shape[1]):
            if np.mod(m + n, 2):
                myImg[m, n] = 0
    return myImg


def myOddIndexSuppression(img):
    myImg = img.copy()
    myImg[::2, 1::2], myImg[1::2, 0::2] = 0, 0
    return myImg


mat = np.ones((5, 5))
res1 = myOddIndexSuppressionLoop(mat)
res2 = myOddIndexSuppression(mat)
print(res1)
print(res2)
