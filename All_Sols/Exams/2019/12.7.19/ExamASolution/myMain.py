__author__ = 'Dmitry Patashov'

from myFunctions import *


qn = 1

if qn == 1:

    n = 2
    myMat = myChessMatrix(n)
    print (myMat)

elif qn == 2:

    myStr = 'Hello Hello We Do Hi no No no we Donot Hey HE he heY nOpe'

    myD = countMyChars(myStr)

    print (myD)

elif qn == 3:

    myList = [1, [2], 3, [1, -1, [2, 5, [1.0], 7.3], 2], -3, 1.0, [[0]]]

    myHist = myListMax(myList)

    print(myHist)

elif qn == 4:

    k = 5
    x = -1.2
    myArray = np.array([-3.2, 8, 1, 0, -1.1, 0.1, 12, -3.5, 0.7])

    myKN  = myKNearest(k, x, myArray)

    print(myKN )

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

elif qn == 7:

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
    plt.imshow(img[:, :, ::-1])
    plt.subplot(122)
    plt.imshow(im[:, :, ::-1])
    plt.show()


elif qn == 8:

    dataMet = np.array([[20, 2],
                        [21, 3],
                        [22, 2],
                        [2, 20],
                        [2, 21],
                        [3, 22],
                        [4, 21],
                        [4, 20]], dtype=np.float64)

    Cs = np.asarray([[np.mean(dataMet[:3,:], axis=0)],
                     [np.mean(dataMet[3:,:], axis=0)]])

    centers = np.array([[20, 3],
                        [2, 22]], dtype=np.float64)

    centers = myKMeansIter(dataMet, centers)

    print centers,'\n\n', Cs

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















