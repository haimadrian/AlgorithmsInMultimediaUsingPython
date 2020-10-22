__author__ = 'Alon Ziv'

import numpy as np, cv2, matplotlib.pyplot as plt


# Ex. A1
def remomve_symbol(st, n):
    if not isinstance(n, int) or n < 1\
        or not isinstance(st, type('')):
        return
    if n > len(st):
        return 'Out of the string!'
    return st[0:n - 1] + st[n:len(st)]


# Ex. A2
def list2matrix(l, n):
    if not isinstance(n, int) or n < 1 or\
       not isinstance(l, type([])):
        return
    if len(l) % n == 0:
        return np.asarray(l).reshape((n, len(l) // n))
    return np.asarray(l)


# Ex. A3
def create_3darray(t):
    if not isinstance(t, type(())) or\
       len(t) != 3 or\
       not all(isinstance(x, int) and x > 0 for x in t):
        return
    return np.ndarray(t)


# Ex. A4
def count_word(st, w):
    if not isinstance(w, type('')) or\
       not isinstance(st, type('')):
        return
    return st.count(w)


# Ex. B1
def PadMyImage(image, size):
    if not isinstance(image, np.ndarray) or\
       not isinstance(size, int) or size < 1:
        return
    img = cv2.copyMakeBorder(image, size, size, size, size, cv2.BORDER_CONSTANT, value=255)
    return img


# Ex. B2
def MaskMyImage(image, mask):
    if not isinstance(image, np.ndarray):
        return
    shape = image.shape
    newImg = np.zeros(shape, dtype=np.float64)
    size = mask.shape[0] // 2
    paddedImg = cv2.copyMakeBorder(image, size, size, size, size, cv2.BORDER_REPLICATE)
    for i in range(shape[0]):
        for j in range(shape[1]):
            newImg[i, j] = np.sum(paddedImg[i:i + mask.shape[0], j:j + mask.shape[1]] * mask)
    return newImg


# Ex. B3
def FunctionPlotter(str):
    if not isinstance(str, type('')) or not str in ('sin', 'cos', 'con', 'All'):
        return
    x = np.linspace(0, 2 * np.pi, 1000)
    plt.figure()
    if str == 'sin':
        plt.plot(x, np.sin(x), 'blue')
    elif str == 'cos':
        plt.plot(x, np.cos(x), 'green')
    elif str == 'con':
        plt.plot(x, np.zeros(x.shape), 'red')
    else:
        plt.plot(x, np.sin(x), 'blue')
        plt.plot(x, np.cos(x), 'green')
        plt.plot(x, np.zeros(x.shape), 'red')
    plt.show()


# Ex. C
def MyCirclePlot(image):
    if not isinstance(image, np.ndarray):
        return
    border = np.zeros((image.shape[0], np.int64(image.shape[1] * 0.2))) + 255
    image = np.concatenate((border, image, border), axis=1)
    plt.figure()
    plt.subplot(511)
    plt.axis('off')
    plt.imshow(image, cmap='gray')
    plt.subplot(515)
    plt.axis('off')
    plt.imshow(image, cmap='gray')
    img2 = np.concatenate((image, image), axis=1)
    plt.subplot(512)
    plt.axis('off')
    plt.imshow(img2, cmap='gray')
    plt.subplot(514)
    plt.axis('off')
    plt.imshow(img2, cmap='gray')
    white = np.zeros(image.shape) + 255
    plt.subplot(513)
    plt.axis('off')
    plt.imshow(np.concatenate((image, white, white, image), axis=1), cmap='gray')