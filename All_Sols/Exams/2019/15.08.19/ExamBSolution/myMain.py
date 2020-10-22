__author__ = 'Dmitry Patashov'

from myFunctions import *


qn = 1

if qn == 1:

    n = 4
    myMat = myTriangularMatrix(n)
    print (myMat)

elif qn == 2:

    myStr = 'Hello Hello We Do Hi no No no we Donot Hey HE he heY nOpe'

    myD = countMyChars(myStr)

    print (myD)

elif qn == 3:

    myList = [1, [2], 3, [1, -1, [2, 5, [1.0], 7.3], 2], -3, 1.0, [[0]]]

    myHist = myListMin(myList)

    print(myHist)

elif qn == 4:

    myPath = os.getcwd()
    myExtention = 'py'

    myKN  = myFileSearch(myPath, myExtention)

    print(myKN )

elif qn == 5:

    img = cv2.imread('sea.jpg')

    im = myBorderCreation(img, 100)

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

elif qn == 8:

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

elif qn == 9:

    time = np.arange(0, 2 * np.pi, 0.01)
    sig = np.sin(time)
    NoisePr = 0.1

    nSig = SaltAndPepperSignalNoise(sig.copy(), NoisePr)

    plt.figure()
    ax1 = plt.subplot(211)
    plt.plot(time, sig, 'k')
    ax2 = plt.subplot(212, sharex=ax1, sharey=ax1)
    plt.plot(time, nSig, 'k')
    plt.show()















