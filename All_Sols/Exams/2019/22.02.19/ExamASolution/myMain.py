__author__ = 'Dmitry Patashov'

from myFunctions import *


qn = 9

if qn == 1:

    n = 2
    myMat = myPlusMatrix(n)
    print (myMat)

elif qn == 2:

    myStr = 'Hello Hello We Do Hi no No no we Donot Hey HE he heY nOpe'

    myD = countMyStrings(myStr)

    print (myD)

elif qn == 3:

    myList = [1, [2], 3, [1, -1, [2, 3, [1.0], 1], 2], -3, 1.0, [[0]]]

    myMean = myListMean(myList)

    print(myMean)

elif qn == 4:

    myList = UpFolderConatin()

    print(myList)

elif qn == 5:

    img = cv2.imread('cat.jpeg')

    im = TwoLiner(img)

    plt.figure()
    plt.imshow(im[:,:,::-1])
    plt.show()

elif qn == 6:

    DataMat = cv2.imread('cat.jpeg', 0)

    myMat = myLinearDependancyRemoval(np.float64(DataMat))

    print(myMat)

elif qn == 7:

    time = np.arange(0, 100, 0.001)
    signal = (time - 50) ** 2

    startLoc = 89
    iterNum = 20
    stepSize = 20

    t1 = myGradDescent(signal, time, startLoc, iterNum, stepSize)

    plt.figure()
    plt.plot(time, signal)
    plt.stem([startLoc], [(startLoc - 50) ** 2], 'g')
    plt.stem([t1], [(t1 - 50) ** 2], 'r')
    plt.show()


elif qn == 8:

    time = np.arange(0, 2 * np.pi, 0.01)
    Sine = np.sin(time)

    L = len(time)
    noise = np.random.uniform(-0.2, 0.2, L)

    signal = Sine + noise
    order = 10

    Sig1 = mySignalFiltering(signal, order, 0)
    Sig2 = mySignalFiltering(signal, order, 1)

    plt.figure()
    plt.subplot(211)
    plt.plot(time, signal)
    plt.subplot(223)
    plt.plot(time, Sig1)
    plt.subplot(224)
    plt.plot(time, Sig2)
    plt.show()

elif qn == 9:

    img = cv2.imread('icon.png', 0)

    im1 = myOddIndexSuppression1(img)
    im2 = myOddIndexSuppression2(img)

    plt.figure()
    plt.subplot(211)
    plt.imshow(img, cmap='gray', interpolation='none')
    plt.subplot(223)
    plt.imshow(im1, cmap='gray', interpolation='none')
    plt.subplot(224)
    plt.imshow(im2, cmap='gray', interpolation='none')
    plt.show()















