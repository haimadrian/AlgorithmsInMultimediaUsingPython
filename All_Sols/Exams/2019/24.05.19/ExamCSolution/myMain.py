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

    myList = [1, [2], 3, [11, 1, [2, 3, [1.0]], 2], 3, 1.0, [[0]]]

    myHist = myListHist(myList)

    print(myHist)

elif qn == 4:

    k = 3
    x = -1.2
    myArray = np.array([-3.2, 8, 1, 0, -1.1, 0.1, 12])

    myKN  = myKNearest(k, x, myArray)

    print(myKN )

elif qn == 5:

    img = cv2.imread('sea.jpg')

    im = myFastToneReplacement(img, 100, 150, 250)

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

    t = np.arange(0,10 * 2*np.pi,0.01)
    sig = 1.1*np.sin(t)

    locs = myPeakDetect(sig.copy())

    plt.figure()
    plt.plot(t, sig, 'k')
    plt.plot(t[locs], sig[locs], 'rx')
    plt.show()















