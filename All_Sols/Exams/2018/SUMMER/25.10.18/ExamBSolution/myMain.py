__author__ = 'Dmitry Patashov'

from myFunctions import *

qn = 9

if qn == 1:

    print myPerimiterMatrix(3), '\n'
    print myPerimiterMatrix(4)

elif qn == 2:

    myStr = 'Hello Hello We Do Hi no No no we Donot Hey HE he heY 123'

    print countMyWords(myStr)

elif qn == 3:

    myList = [1, [2], 3, [1, -1, [2, 3, [1.0], 1], 2], -3, 1.0, 2.0]
    print myListSum(myList)

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

    k = 3
    a = np.array([[0.6787, 0.7431, 0.6555, 0.7060, 0.2769, 0.0971, 0.6948, 0.9502, 0.4387, 0.7655,
                   0.1869, 0.4456, 0.7094, 0.2760, 0.6551, 0.1190, 0.9597, 0.5853, 0.7513, 0.5060,
                   0.8909, 0.5472, 0.1493, 0.8407, 0.8143, 0.9293, 0.1966, 0.6160, 0.3517, 0.5853],
                  [0.7577, 0.3922, 0.1712, 0.0318, 0.0462, 0.8235, 0.3171, 0.0344, 0.3816, 0.7952,
                   0.4898, 0.6463, 0.7547, 0.6797, 0.1626, 0.4984, 0.3404, 0.2238, 0.2551, 0.6991,
                   0.9593, 0.1386, 0.2575, 0.2543, 0.2435, 0.3500, 0.2511, 0.4733, 0.8308, 0.5497]], np.float64)

    b = np.array([[0.7018, 0.5399, 0.4839, 0.7173, 1.2027, 0.7909, 0.6377, 0.6692, 1.0803, 0.5417,
                   0.3965, 1.2421, 0.8752, 0.5348, 1.1212, 0.3430, 0.9491, 0.9477, 0.8470, 1.0447,
                   0.9868, 0.6685, 1.0802, 1.2294, 0.7868, 0.7468, 0.8085, 1.1176, 0.9443, 1.1116],
                  [0.3760, 0.4233, 0.5400, 0.3497, 1.2448, 0.7893, 1.2001, 0.4112, 0.6897, 0.7039,
                   0.4320, 1.2561, 0.3598, 0.6532, 0.3154, 0.4690, 1.0317, 0.7509, 0.5963, 0.4890,
                   0.4835, 0.9256, 0.3811, 1.0757, 0.7359, 0.6063, 0.8108, 1.0948, 0.6786, 0.8328]], np.float64)

    Data = np.concatenate((a.transpose(), b.transpose()), 0)
    Labels = np.concatenate((np.zeros((a.shape[1], 1)), np.ones((b.shape[1], 1))), 0)
    Sample1 = np.array([[0.5, 0.5]], np.float64)
    Sample2 = np.array([[0.9, 0.3]], np.float64)

    myLabel1 = myKNNClasification(k, Data, Labels, Sample1)
    myLabel2 = myKNNClasification(k, Data, Labels, Sample2)

    print myLabel1, myLabel2

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

    myMat = np.round(np.random.uniform(0, 180, (5, 5)) * 100) / 100
    print myMat, '\n'
    print myPhaseRound(myMat)

elif qn == 9:

    img = cv2.imread('im.jpeg')
    myPlotShape(img[:,:,[1,0,2]])

