__author__ = "Haim Adrian"

import matplotlib

# Do it to see a new window when calling plt.show, and not within PyCharm.
matplotlib.use('TkAgg')
from Functions import *


def ex1Test():
    print("ex1: (myMasking)")
    originalMatrix = np.array([[170, 238, 85, 255, 221, 0],
                               [68, 136, 17, 170, 119, 68],
                               [221, 0, 238, 136, 0, 255],
                               [119, 255, 85, 170, 136, 238],
                               [238, 17, 221, 68, 19, 255],
                               [85, 170, 119, 221, 17, 136]])
    mask = (1 / 9) * np.ones((3, 3))
    result = myMasking(originalMatrix, mask)
    
    print("Original:")
    print(originalMatrix)
    print("Mask:")
    print(mask)
    print("Result:")
    print(result)


def ex1():
    img = cv2.imread("Cat.jpg")
    # Mask sum is 1, then we will need to normalize, round and cast.
    gaussianMask = (1 / 16) * np.array([[1, 2, 1],
                                        [2, 4, 2],
                                        [1, 2, 1]])
    # Mask sum is 0, then we will need to use absolute before normalizing the image
    laplacianMask = np.array([[0, -1, 0],
                              [-1, 4, -1],
                              [0, -1, 0]])

    gaussian = normalizeImage(myMasking(img, gaussianMask))
    laplacian = normalizeImage(np.abs(myMasking(img, laplacianMask)))

    plt.figure('Masking')
    plt.subplot(131)
    plt.imshow(img[:, :, ::-1])
    plt.axis('off')
    plt.title('Original')
    plt.subplot(132)
    plt.imshow(gaussian[:, :, ::-1])
    plt.axis('off')
    plt.title('Gaussian')
    plt.subplot(133)
    plt.imshow(laplacian[:, :, ::-1])
    plt.axis('off')
    plt.title('Laplacian')
    plt.show()


def ex2():
    img, masked = someMask()

    plt.figure('EX2 - BlurryImage')
    plt.subplot(121)
    plt.imshow(img[:, :, ::-1])
    plt.axis('off')
    plt.title('Original')
    plt.subplot(122)
    plt.imshow(masked[:, :, ::-1])
    plt.axis('off')
    plt.title('Masked')
    plt.show()


def ex3():
    img, masked = someMask()
    myHistPlot(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY))


def ex4():
    # Median filter sum is either 0 or 1, so we will need to use absolute, round and cast (normalizing image)
    img, medianFiltered = medianFilter()
    img = normalizeImage(img[:, :, ::-1])
    medianFiltered = normalizeImage(np.abs(medianFiltered[:, :, ::-1]))

    plt.figure('EX4 - Median and Gaussian')
    plt.subplot(221)
    plt.imshow(img)
    plt.colorbar(ticks=np.arange(0, 1.1, 0.2), orientation='horizontal')
    plt.axis('off')
    plt.title('Original')
    plt.subplot(222)
    plt.imshow(medianFiltered)
    plt.colorbar(ticks=np.arange(0, 1.1, 0.2), orientation='horizontal')
    plt.axis('off')
    plt.title('Median And Gaussian')
    plt.subplot(223)
    plt.hist(img.ravel(), bins=256, color='b', fc='k', ec='k')
    plt.title('Histogram')
    plt.subplot(224)
    plt.hist(medianFiltered.ravel(), bins=256, color='b', fc='k', ec='k')
    plt.title('Histogram')
    plt.show()


def ex5():
    # exec(open('Debugging.py').read())
    import Debugging as db
    db.doSomething()
    print()


# ex1Test()
# ex1()
# ex2()
# ex3()
# ex4()
ex5()
