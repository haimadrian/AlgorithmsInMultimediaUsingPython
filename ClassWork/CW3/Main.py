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
    img = fuck(cv2.imread('img1.jpg'))
    cv2.imshow('myExtendedPadding', img)
    cv2.waitKey()
    print()


ex1()
ex2()
ex3()
ex4()
ex5()
ex6()
ex7()
ex8()
ex9()
ex10()
ex11()
ex12()
