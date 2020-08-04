__author__ = "Haim Adrian"

import numbers
import os
import sys
import numpy


# Assignment 1
def myList2Text(lst):
    if lst.__class__ != [].__class__:
        return None

    return ''.join(str(item) for item in lst)


# Assignment 2
def isNumeric(x):
    return isinstance(x, numbers.Number)


def myListMean(lst):
    if lst.__class__ != [].__class__:
        return None

    count = 0
    summ = 0

    for item in lst:
        if isNumeric(item):
            count += 1
            summ += item

    if count > 0:
        avgg = summ / count
        # Maximum value representable by a Word. maxsize is signed. Calculate unsigned
        closestRange = sys.maxsize * 2 + 1
        selectedItem = None
        for i in range(len(lst)):
            item = lst[i]
            if isNumeric(item) and abs(item - avgg) < closestRange:
                selectedItem, closestRange = i, abs(item - avgg)

        print("Mean of numeric items: " + str(avgg))
        print("Index of closest item (to mean) is: " + str(selectedItem))
    else:
        print("No numbers in specified list")


# Assignment 3
def list_files(dirr=os.getcwd()):
    if not os.path.exists(dirr):
        print("Directory {} does not exist".format(dirr))
        return None

    if not os.path.isdir(dirr):
        print("{} is not a directory".format(dirr))
        return None

    files = [f for f in os.listdir(dirr) if os.path.isfile(os.path.join(dirr, f))]
    return files


# Assignment 4
def create_3darray(shape):
    if shape.__class__ != ().__class__:
        return None

    return numpy.zeros(shape)


# Assignment 5
def myRot13(text):
    if text.__class__ != "".__class__:
        return None

    if not hasattr(myRot13, 'alphabet'):
        myRot13.alphabet = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u',
                            'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c',
                            'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k',
                            'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S',
                            'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A',
                            'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I',
                            'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}

    result = ""
    for i in range(len(text)):
        char = text[i]

        # Skip escaped characters
        if char == '\\':
            i += 1
            continue

        if char in myRot13.alphabet:
            result += myRot13.alphabet[char]
        else:
            result += char
    return result


# Assignment 6
def countMyWords(text):
    if text.__class__ != "".__class__:
        return None

    wordCounts = {}
    words = str(text).split()
    for word in [i.lower() for i in words]:
        wordCounts[word] = 1 if word not in wordCounts else wordCounts[word] + 1

    return wordCounts


# Assignment 7
def robot_dist(up, down, left, right, originalPoint=(0, 0)):
    current = (up - down, right - left)
    print("Source: " + str(originalPoint))
    print("Dest: " + str(current))

    dist = numpy.linalg.norm(numpy.array(current) - numpy.array(originalPoint))

    # angle = ArcTangent(deltaY / deltaX)
    radians = numpy.arctan2(current[1] - originalPoint[1], current[0] - originalPoint[0])
    return dist, radians

