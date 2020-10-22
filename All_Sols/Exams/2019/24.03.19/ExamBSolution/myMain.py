__author__ = 'Dmitry Patashov'

from myFunctions import *


qn = 3

if qn == 1:

    n = 2
    myMat = myPlusMatrix(n)
    print (myMat)

elif qn == 2:

    myStr = 'Hello Hello We Do Hi no No no we Donot Hey HE he heY nOpe'

    myD = countMyStrings(myStr)

    print (myD)

elif qn == 3:

    myList = [1, [2], 3, [11, -1, [2, 3, [1.0]], 2], -3, 1.0, [[0]]]

    myMean = myListMedian(myList)

    print(myMean)

elif qn == 4:

    myList = UpFolderContain()

    print(myList)

elif qn == 5:

    img = cv2.imread('sea.jpg')

    im = myColorShift(img)

    plt.figure()
    plt.subplot(121)
    plt.imshow(img[:, :, ::-1])
    plt.subplot(122)
    plt.imshow(im[:,:,::-1])
    plt.show()

elif qn == 6:

    print('\nLoading Data')
    import pandas as pd

    df = pd.read_excel('miniRowDataMat.xlsx')
    lf = pd.read_excel('miniLabelVec.xlsx')
    print('Data Loading Complete\n')

    TrainData = df.values
    TrainLabel = lf.values
    W = np.random.uniform(0, np.max(TrainData), (TrainData.shape[1],1))
    gamma = 0.01
    Itterations = 10 ** 3

    W = myLRcycles(TrainData, TrainLabel, W, gamma, Itterations)

    print(W)

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

    # img = cv2.imread('plains.jpg', 0)
    img = cv2.imread('plains.jpg')
    rad = 100

    im = myDiagEdgeDetect(img, rad)

    # plt.figure()
    # plt.subplot(121)
    # plt.imshow(img, cmap='gray')
    # plt.axis('off')
    # plt.subplot(122)
    # plt.imshow(im, cmap='gray')
    # plt.axis('off')
    # plt.show()

    plt.figure()
    plt.subplot(121)
    plt.imshow(img[:,:,::-1])
    plt.subplot(122)
    plt.imshow(im[:, :, ::-1])
    plt.show()

elif qn == 9:

    time = np.arange(0,2*np.pi,0.01)
    sig = np.sin(time)
    NoisePr = 0.1

    nSig = SaltAndPepperSignalNoise(sig.copy(), NoisePr)

    plt.figure()
    ax1 = plt.subplot(211)
    plt.plot(time, sig, 'k')
    ax2 = plt.subplot(212, sharex=ax1, sharey=ax1)
    plt.plot(time, nSig, 'k')
    plt.show()















