__author__ = 'Dmitry Patashov'

from myFunction import *


qn = 2

if qn == 1:

    print '\n', myCrossMatrix(3)
    print '\n', myCrossMatrix(4)

elif qn == 2:

    myList1 = [1, [3.1], 2.0, 'number', (13, 3), ['hello', 8], np.uint8(12), '20']
    print '\n', myListMedian(myList1)

    myList2 = [0, tuple([18]), '12', 0, 10.0, [1, 23], 13.12]
    print '\n', myListMedian(myList2)

elif qn == 3:

    myVal = [1, 2, 3, 'a']
    myKey = ['b', 'c', 'd', 12.3]
    myDict = myDictConst(myKey, myVal)
    print '\n', myDict
    print myDict[12.3]

elif qn == 4:

    myL = [1, 2, 3]
    myL1 = myListEdit(myL, 10, 0)
    print '\n', myL, hex(id(myL)), '\n', myL1, hex(id(myL1))

    myList = [1, 2, 3]
    myList1 = myListEdit(myList, 10, 1)
    print '\n', myList, hex(id(myList)), '\n', myList1, hex(id(myList1))

elif qn == 5:

    img = cv2.imread('index.png')
    im = myColorReplacement(img, 10, 70, 50)

    plt.figure()
    plt.imshow(im[:,:,::-1])
    plt.show()

elif qn == 6:

    img = cv2.imread('snp.png',0)
    im1 = myMedianFilt(img, 1)
    im2 = myMedianFilt(img, 3)
    im3 = myMedianFilt(img, 10)

    plt.figure()
    plt.subplot(221)
    plt.title('Original')
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.subplot(222)
    plt.title('Median 1st order')
    plt.imshow(im1, cmap='gray')
    plt.axis('off')
    plt.subplot(223)
    plt.title('Median 3rd order')
    plt.imshow(im2, cmap='gray')
    plt.axis('off')
    plt.subplot(224)
    plt.title('Median 10th order')
    plt.imshow(im3, cmap='gray')
    plt.axis('off')
    plt.show()

elif qn == 7:

    img = cv2.imread('im.jpeg', 0)
    IntGradMat, PhaseMat = myPolarGradient(img)

    im = IntGradMat.copy()
    im = im - np.min(im)
    im = im / np.max(im) * 255
    im = np.uint8(im)
    plt.figure()
    plt.imshow(im, cmap='gray')
    plt.axis('off')
    plt.show()

elif qn == 8:

    img = cv2.imread('im.jpeg')
    im = myHistEq(img)

    plt.figure()
    plt.subplot(121)
    plt.imshow(img[:, :, ::-1])
    plt.axis('off')
    plt.subplot(122)
    plt.imshow(im[:,:,::-1])
    plt.axis('off')
    plt.show()

elif qn == 9:

    img = cv2.imread('im.jpeg')
    myPlotShape(img)












