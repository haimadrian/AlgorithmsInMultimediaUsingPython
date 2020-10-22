__author__ = 'Alon Ziv'

import numpy as np, numbers, os, cv2, matplotlib.pyplot as plt


# Ex. A1
def remove_symbol(st, n):
    if not isinstance(st, type('')) or\
       not isinstance(n, int) or n < 1:
        return
    if n > len(st):
        return 'Out of the string!'
    return st[0:n-1] + st[n:len(st)]


# Ex. A2
def Matrix2List(mat):
    if not isinstance(mat, np.ndarray):
        return
    return list(mat.reshape(mat.size))


# Ex. A3
def Farthest2Mean(l):
    if not isinstance(l, type([])):
        return
    return np.argmax(np.abs(np.asarray(l) - np.mean(l)))


# Ex. A4
def count_word(st, w):
    if not isinstance(st, type('')) or not isinstance(w, type('')):
        return
    return st.count(w)


# Ex. B1
def ReflectMyImage(img):
    if not isinstance(img, np.ndarray):
        return
    return img[::-1, :, :], img[:, ::-1, :]


# Ex. B2
def most_common_tone(img):
    if not isinstance(img, np.ndarray):
        return
    return np.argmax(np.bincount(img.reshape(img.size)))


# Ex. B3
def FunctionPlotter(f):
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
    plt.show()


# Ex. C
def MyCirclePlot(img):
    if not isinstance(img, np.ndarray):
        return
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plt.figure()

    plt.subplot(511)
    plt.imshow(img, cmap='gray')

    plt.subplot(515)
    plt.imshow(img, cmap='gray')

    plt.subplot(523)
    plt.imshow(img, cmap='gray')

    plt.subplot(524)
    plt.imshow(img, cmap='gray')

    plt.subplot(527)
    plt.imshow(img, cmap='gray')

    plt.subplot(528)
    plt.imshow(img, cmap='gray')

    plt.subplot(549)
    plt.imshow(img, cmap='gray')

    plt.subplot(5, 4, 12)
    plt.imshow(img, cmap='gray')

    plt.show()