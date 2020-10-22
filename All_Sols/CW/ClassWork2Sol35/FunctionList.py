__author__ = 'Dmitry Patashov'

import numpy as np
import numbers
import operator
import os

# Assignment 1:
def myList2Text(myList):

    if myList.__class__ != [].__class__:
        return None

    myStr = ''
    for k in range(len(myList)):
        myStr += str(myList[k])

    return myStr

# Assignment 2:
def myListMean(myList):

    if myList.__class__ != [].__class__:
        return None

    MyL = enumerate(myList)
    subL = list()
    subLind = list()
    for Instance in MyL:
        x = Instance[1]
        tst = isinstance(x, numbers.Number)
        if tst:
            subL.append(Instance[1])
            subLind.append(Instance[0])

    meanVal = np.float64(sum(subL)) / np.float64(len(subL))
    Dist = np.absolute(meanVal - subL)
    Location = subLind[min(enumerate(Dist), key=operator.itemgetter(1))[0]]

    print ('Mean Value =', meanVal, 'Location =', Location)

# Assignment 3:
def list_files(directory=None):

    if directory == None:
        directory = os.getcwd()

    if os.path.exists(directory) == False:
        directory = os.getcwd()
        print ('Error: Directory does not exist!')

    return [x for x in os.listdir(directory) if os.path.isfile(os.path.join(directory, x))]

# Assignment 4:
def create_3darray(myTuple):

    if myTuple.__class__ != tuple('0').__class__:
        return None

    return np.zeros(myTuple)

# Assignment 5:
def myRot13(myText):

    if myText.__class__ != ''.__class__:
        return None

    key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u',
           'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c',
           'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k',
           'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S',
           'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A',
           'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I',
           'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}

    result = ''
    for x in myText:
        if ord(x) >= ord('a') and ord(x) <= ord('z') or ord(x) >= ord('A') and ord(x) <= ord('Z'):
            result += key[x]
        else:
            result += x
    return result

# Assignment 6:
def countMyWords(myStr):

    if myStr.__class__ != ''.__class__:
        return None

    Dist = ord('A') - ord('a')
    myList = list(myStr)
    for k in range(len(myStr)):
        if ord(myStr[k]) >= ord('A') and ord(myStr[k]) <= ord('Z'):
            myList[k] = chr(ord(myStr[k]) - Dist)

    newStr = "".join(myList)
    tmpList = newStr.split()

    ResD = {}
    while len(tmpList):
        ResD[tmpList[0]] = tmpList.count(tmpList[0])
        tmpList = list(filter(lambda a: a != tmpList[0], tmpList))

    print ("{:<20} {}".format('Word', 'Occurrences'))
    for myKey, myLabel in ResD.items():
        print ("{:<20} {}".format(myKey, myLabel))

# Assignment 7:
def robot_dist(up, down, left, right):

    xcount = 0
    if up.__class__ != xcount.__class__ or \
        down.__class__ != xcount.__class__ or \
        left.__class__ != xcount.__class__ or \
        right.__class__ != xcount.__class__:

        return None

    ycount = up - down
    xcount = right - left

    Distance = (ycount ** 2 + xcount ** 2) ** 0.5
    Angle = np.arctan2(ycount, xcount)

    return Distance, Angle

