__author__ = "Haim Adrian"

import matplotlib

# Do it to see a new window when calling plt.show, and not within PyCharm.
matplotlib.use('TkAgg')

from Functions import *


def ex1():
    print("ex1: (showImageTwice)")
    imgName = 'img1.jpg'
    showImageTwice(imgName)
    print()


def ex2():
    print("ex2: (myBGR2RGB)")
    print()


def ex3():
    print("ex3: (splitRGB)")
    splitRGB()
    print()


def ex4():
    print("ex4: (drawGreenHorizontalLine)")
    img = drawGreenHorizontalLine(cv2.imread('img4.jpeg'))
    cv2.imshow('drawGreenHorizontalLine', img)
    cv2.waitKey()
    print()


def ex5():
    print("ex5: (drawRedDiagonalLine)")
    img = drawRedDiagonalLine(cv2.imread('img4.jpeg'))
    cv2.imshow('drawRedDiagonalLine', img)
    cv2.waitKey()
    print()


def ex6():
    print("ex6: (drawBlueSquare)")
    img = drawBlueSquare(cv2.imread('img4.jpeg'))
    cv2.imshow('drawBlueSquare', img)
    cv2.waitKey()
    print()


def ex7():
    print("ex7: (drawPurpleCircle)")
    img = drawPurpleCircle(cv2.imread('img4.jpeg'))
    cv2.imshow('drawPurpleCircle', img)
    cv2.waitKey()
    print()


def ex8():
    print("ex8: (drawTriangle)")
    img = drawTriangle(cv2.imread('img4.jpeg'))
    cv2.imshow('drawTriangle', img)
    cv2.waitKey()
    print()


def ex9():
    print("ex9: (drawGrayscale)")
    drawGrayscale()
    print()


def ex10():
    print("ex10: (myZeroPadding)")
    img = myZeroPadding2(cv2.imread('img1.jpg'), 50)
    cv2.imshow('myZeroPadding', img)
    cv2.waitKey()
    print()


def ex11():
    print("ex11: (myExtendedPadding)")
    img = myExtendedPadding2(cv2.imread('img1.jpg'), 50)
    cv2.imshow('myExtendedPadding', img)
    cv2.waitKey()
    print()


def ex12():
    print("ex12: (WTF)")
    img = fuck(cv2.cvtColor(cv2.imread('trunks.jpg'), cv2.COLOR_BGR2GRAY))
    cv2.imshow('myExtendedPadding', img)
    cv2.waitKey()
    print()


# ex1()
# ex2()
# ex3()
# ex4()
# ex5()
# ex6()
# ex7()
# ex8()
# ex9()
# ex10()
# ex11()
# ex12()

def test():
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3, 4, 5]

    a += [6, 7]
    b = b + [6, 7]

    print(a)
    print(b)

    vec = np.zeros(3)
    mat = np.zeros((1, 3))
    print(vec)
    print(mat)

    myMat = np.zeros((3, 3), int)
    np.fill_diagonal(myMat, 1)
    np.fill_diagonal(np.fliplr(myMat), 1)
    print(myMat)


def myPlusMatrix(n):
    matt = np.zeros((2*n + 1, 2*n + 1), dtype=np.int8)
    matt[n, :] = 1
    matt[:, n] = 1
    return matt


mat = myPlusMatrix(1)
print(mat)

# for i in enum:
#    print(i)
#    print(i[0])
