__author__ = "Haim Adrian"

import matplotlib
import numpy as np
from numbers import Number


def myChessMatrix(n):
    mat = np.zeros((2*n, 2*n))
    mat[1::2, ::2], mat[::2, 1::2] = 1, 1
    return mat


def countMyChars1(string):
    string = string.lower()
    counts = {c: string.count(c) for c in set(string)}
    return counts


def countMyChars2(string):
    string = string.lower()
    counts = {}
    while string:
        counts[string[0]] = string.count(string[0])
        string = string.replace(string[0], '')
    return counts


# count1 = countMyChars1('Hello Hello We Do Hi no No no we Donot Hey HE he heY')
# print(count1)
# count2 = countMyChars2('Hello Hello We Do Hi no No no we Donot Hey HE he heY')
# print(count2)


def myListHist(lst):
    def flattenList(lst_inner):
        result = []
        for i in lst_inner:
            if (isinstance(i, int)) or (isinstance(i, float) and i.is_integer()):
                result.append(int(i))
            elif isinstance(i, list):
                result.extend(flattenList(i))
        return result

    flattenedList = flattenList(lst)
    hist = np.zeros(int(np.max(flattenedList) + 1), dtype=np.uint64)
    for i in set(flattenedList):
        hist[i] = flattenedList.count(i)
    return hist


myList = [1, [2], 3, [11, 1, [2, 3, [1.0]], 2], 3, 1.0, [[0]]]
myHist = myListHist(myList)
print(myHist)
