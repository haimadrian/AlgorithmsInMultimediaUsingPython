import numpy as np


def MaxOfThree(a, b, c):
    x = np.float64(a)
    y = np.float64(b)
    z = np.float64(c)

    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z


def mySum(inList):
    newList = np.float64(inList)

    sumres = 0.0
    for x in newList:
        sumres += x
    return sumres


def myMultiply(inList):
    newList = np.float64(inList)

    mulres = 1.0
    for x in newList:
        mulres *= x
    return mulres


def myMean():
    sumRes = 0.0
    amm = 0.0
    flag = True
    while flag:
        x = input('Enter number: ')
        flag = x.replace('.','',1).replace('-','',1).isdigit()
        if '-' in x and not x.startswith('-'):
            flag = False
        if flag:
            amm += 1
            sumRes += np.float64(x)
    if amm:
        return sumRes/amm
    else:
        return 0


def myStars(intList):
    for x in intList:
        stars = '*' * x
        print(stars)


def mySecondBest(inList):
    newList = np.float64(inList)

    top = np.max([newList[0], newList[1]])
    secondTop = np.min([newList[0], newList[1]])
    bottom = secondTop
    secondBottom = top

    for i in range(1,len(newList)):
        if top < newList[i]:
            secondTop = top
            top = newList[i]
        elif secondTop < newList[i]:
            secondTop = newList[i]

        if bottom > newList[i]:
            secondBottom = bottom
            bottom = newList[i]
        elif secondBottom > newList[i]:
            secondBottom = newList[i]

    return secondTop, secondBottom


def mySort(charList):

    myArrL = np.zeros((1, 26))
    myArrU = np.zeros((1, 26))

    for ch in charList:
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            myArrL[0, ord(ch) - ord('a')] += 1
        elif ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
            myArrU[0, ord(ch) - ord('A')] += 1
        else:
            return None

    newChList = list()
    for k in range(26):
        while myArrU[0,k]:
            newChList.append(chr(ord('A') + k))
            myArrU[0,k] -= 1

    for k in range(26):
        while myArrL[0,k]:
            newChList.append(chr(ord('a') + k))
            myArrL[0,k] -= 1

    return newChList


# # Question 7, solution 1
# def myChar2Num(charList):
#     letterNum = list()
#     for ch in charList:
#         if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
#             letterNum.append(ord(ch) - ord('a') + 1)
#         elif ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
#             letterNum.append(ord(ch) - ord('A') + 1)
#         else:
#             return None
#     return letterNum


# Question 7, solution 2
def myChar2Num(charList):
    return [ord(ch.lower()) - ord('a') + 1 for ch in charList]
