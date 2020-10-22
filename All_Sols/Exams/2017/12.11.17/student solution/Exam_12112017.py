__author__ = 'Alon Ziv'

import numpy as np, os, matplotlib.pyplot as plt
from collections import Counter


# Ex. 1
def myFullTensor(dim):
    if not isinstance(dim, type(()))\
            or not all(isinstance(x, int) for x in dim)\
            or any(x <= 0 for x in dim):
        return
    return np.ones(dim) * 7.5


# Ex. 2
def myFilesList(dir=os.getcwd()):
    if not isinstance(dir, type('')):
        return
    if not os.path.exists(dir):
        dir = os.getcwd()
    return [file for file in os.listdir(dir) if os.path.isfile(os.path.join(dir, file))]


# Ex. 3
def myImageMean(img):
    if not isinstance(img, np.ndarray):
        return
    return np.float64(np.mean(img))


# Ex. 4
def myCommonTone(img):
    if not isinstance(img, np.ndarray):
        return
    # sol 1
    # counts = np.ndarray(256)
    # img = np.uint8(img)
    # for i in range(256):
    #     counts[i] = len(img[img == i])
    # return np.argmax(counts)
    # sol 2
    # return Counter(np.uint8(img.reshape(img.size))).most_common(1)[0][0]
    # sol 3
    return np.argmax(np.bincount(np.uint8(img.reshape(img.size))))


# Ex. 5
def myLine(img):
    myImg = img.copy()
    center = myImg.shape[0] // 2
    myImg[center - 30: center + 40, :, 2] = 0
    return myImg


# Ex. 6
def myPhaseRound(mat):
    if not isinstance(mat, np.ndarray):
        return
    r = 45 / 2
    steps = range(0, 181, 45)
    for value in steps:
        low = steps[0] if value == steps[0] else value - r - 1
        high = steps[-1] if value == steps[-1] else value + r
        mat[np.logical_and(mat >= low, mat <= high)] = value % 180
    return mat


# Ex. 7
def myDataSplit(data):
    if not isinstance(data, np.ndarray) or data.shape[0] != 100:
        return
    a, b, c = data[:5, :], data[5:8, :], data[8:10, :]
    for i in range(10, 100, 10):
        a = np.concatenate((a, data[i: i + 5, :]))
        b = np.concatenate((b, data[i + 5: i + 8, :]))
        c = np.concatenate((c, data[i + 8: i + 10, :]))
    return a, b, c


# Ex. 8
def myFunctionPlotter(f):
    if not isinstance(f, type('')) or not f in ('sin', 'cos', 'con', 'All'):
        return
    x = np.linspace(0, 2 * np.pi, 1000)
    plt.figure()
    if f == 'sin':
        plt.plot(x, np.sin(x), 'blue')
    elif f == 'cos':
        plt.plot(x, np.cos(x), 'green')
    elif f == 'con':
        plt.plot(x, np.zeros(x.shape), 'red')
    else:
        plt.plot(x, np.sin(x), 'blue')
        plt.plot(x, np.cos(x), 'green')
        plt.plot(x, np.zeros(x.shape), 'red')


# Ex. 9
def myPlotShape(img):
    if not isinstance(img, np.ndarray):
        return
    plt.figure()
    border = np.ones((np.int64(img.shape[0] * 0.15), img.shape[1])) * 255
    img = np.concatenate((border, img, border))
    plt.subplot(141)
    plt.axis('off')
    plt.imshow(img, cmap='gray')
    plt.subplot(142)
    plt.axis('off')
    plt.imshow(np.concatenate((img, img)), cmap='gray')
    plt.subplot(143)
    plt.axis('off')
    white = np.ones(img.shape) * 255
    plt.imshow(np.concatenate((img, white, white, img)), cmap='gray')
    plt.subplot(144)
    plt.axis('off')
    plt.imshow(np.concatenate((img, img, img, img, img)), cmap='gray')
    plt.show()
