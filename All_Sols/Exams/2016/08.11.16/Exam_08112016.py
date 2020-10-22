__author__ = 'Alon Ziv'

import numpy as np, numbers, os, cv2, matplotlib.pyplot as plt


# Ex. A1

def f(myList):
    if not isinstance(myList,type([])):
        return None
    for x in myList:
        n= myList.count(x)
        if n>1:
            for i in range(n-1):
                myList.remove(x)

    return myList





def Remove_Duplicates(MyList):
    if not isinstance(MyList, type([])):
        return
    for el in MyList:
        n = MyList.count(el)
        if n > 1:
            for i in range(n - 1):
                MyList.remove(el)

    return list(set(MyList))


# Ex. A2
def Matrix2List(MyMat):
    if not isinstance(MyMat, np.ndarray):
        return
    return list(MyMat.reshape(MyMat.size))


# Ex. A3
def Nearest2Mean(MyList):
    if not isinstance(MyList, type([])) or\
       not all(isinstance(x, numbers.Number) for x in MyList):
        return
    return np.argmin(np.abs(np.asarray(MyList)-np.mean(MyList)))

    return np.argmin(np.abs(np.asarray(MyList) - np.mean(MyList)))


# Ex. A4
def List_Files(MyDir=os.getcwd()):
    if not isinstance(MyDir, type('')):
        return
    if os.path.exists(MyDir) == False:
        MyDir = os.getcwd()
    return [file for file in os.listdir(MyDir) if os.path.isfile(os.path.join(MyDir, file))]


# Ex. B1
def MedianFilter(img, size):
    if not isinstance(img, np.ndarray) or\
       not isinstance(size, int) or size < 1:
        return
    shape = img.shape
    newImg = np.zeros(shape)
    paddedImg = cv2.copyMakeBorder(img, size, size, size, size, cv2.BORDER_CONSTANT, value=0)
    wind = 2 * size + 1
    for i in range(shape[0]):
        for j in range(shape[1]):
            newImg[i, j] = np.median(paddedImg[i:i + wind, j:j + wind])
    return newImg


# Ex. B2
def ReflectMyImgae(img):
    if not isinstance(img, np.ndarray):
        return
    return img[::-1, :, :], img[:, ::-1, :]


# Ex. B3
def FunctionPlotter(MyStr):
    if not isinstance(MyStr, type('')) or not MyStr in ('exp', 'log', 'con', 'All'):
        return
    x = np.linspace(0.01, 10, 1000)
    plt.figure()
    plt.title(MyStr)
    if MyStr == 'exp':
        plt.plot(x, np.exp(x), 'blue')
    elif MyStr == 'log':
        plt.plot(x, np.log(x), 'green')
    elif MyStr == 'con':
        plt.plot(x, np.zeros(x.shape), 'red')
    else:
        plt.plot(x, np.exp(x), 'blue')
        plt.plot(x, np.log(x), 'green')
        plt.plot(x, np.zeros(x.shape), 'red')
    plt.show()


# Ex. C
def MyCircleImagePlot(img):
    if not isinstance(img, np.ndarray):
        return
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.figure()

    plt.subplot(5, 7, 2)
    plt.imshow(img)

    plt.subplot(5, 7, 6)
    plt.imshow(img)

    plt.subplot(5, 7, (8, 9))
    plt.imshow(img)

    plt.subplot(5, 7, 11)
    plt.imshow(img)

    plt.subplot(5, 7, (13, 14))
    plt.imshow(img)

    plt.subplot(5, 7, 15)
    plt.imshow(img)

    plt.subplot(5, 7, 18)
    plt.imshow(img)

    plt.subplot(5, 7, 21)
    plt.imshow(img)

    plt.subplot(5, 7, (22, 23))
    plt.imshow(img)

    plt.subplot(5, 7, 25)
    plt.imshow(img)

    plt.subplot(5, 7, (27, 28))
    plt.imshow(img)

    plt.subplot(5, 7, 30)
    plt.imshow(img)

    plt.subplot(5, 7, 34)
    plt.imshow(img)

    plt.show()