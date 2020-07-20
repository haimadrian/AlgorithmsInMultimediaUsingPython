from random import randrange


def maxOfThree(a, b, c):
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    elif b >= c:
        return b
    else:
        return c


def mySum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum


def myMul(arr):
    mul = 1
    for i in arr:
        mul *= i
    return mul


def isNumeric(x):
    import re

    # Store a compiled regex onto the function so we will not have to recompile it over and over
    if not hasattr(myMean, 'isNumeric'):
        isNumeric.numericRegex = re.compile(r"^([+-]?\d*)\.?\d*$")
    return len(str(x).strip()) > 0 and isNumeric.numericRegex.match(str(x).strip()) is not None


def myMean():
    count = 0
    summ = 0
    x = input("Enter a number: ")
    while isNumeric(x):
        count += 1
        summ += float(x)
        x = input("Enter a number: ")

    return 0 if count == 0 else (summ / count)


def myStars(arr):
    for i in arr:
        print(''.join('*' for j in range(i)))


def secondBest(arr):
    maxx = [None, None]
    minn = [None, None]

    if len(arr) < 2:
        return None

    if arr[0] > arr[1]:
        minn[1] = maxx[0] = arr[0]
        minn[0] = maxx[1] = arr[1]
    else:
        minn[1] = maxx[0] = arr[1]
        minn[0] = maxx[1] = arr[0]

    for i in arr[2::]:
        if i > maxx[0]:
            maxx[1] = maxx[0]
            maxx[0] = i

        if i < minn[0]:
            minn[1] = minn[0]
            minn[0] = i

    return [maxx[1], minn[1]]


def randPartition(arr, low, high):
    pivotIndex = randrange(low, high + 1)
    arr[pivotIndex], arr[high] = arr[high], arr[pivotIndex]
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i


def mySort(arr, low, high):
    if low < high:
        p = randPartition(arr, low, high)
        mySort(arr, low, p-1)
        mySort(arr, p+1, high)


def myChar2Num(arr):
    return [(ord(i) - ord('a') + 1) for i in arr]

