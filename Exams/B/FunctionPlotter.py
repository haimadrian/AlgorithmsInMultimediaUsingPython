# 305265514
__author__ = "Haim Adrian"

import numpy as np
from matplotlib import pyplot as plt


def FunctionPlotter(func='sqr'):
    if func not in ['x^2', 'sqr', 'lnx', 'All']:
        return None

    def xSquare(xs):
        return 0.5 * (xs ** 2) + 1.5 * xs + 7

    def lnx(xs):
        return 200 * np.log(xs - 3)

    def sqr(xs):
        return (0.01 * (xs ** 5) + 1.5) ** 0.5

    x = np.arange(10, 50, 1/15)
    plt.figure()
    plt.title(func)
    plt.xlabel('time[sec]')
    plt.ylabel('amplitude')
    if func == 'x^2' or func == 'All':
        plt.plot(x, xSquare(x), 'red')

    if func == 'lnx' or func == 'All':
        plt.plot(x, lnx(x), 'black')

    if func == 'sqr' or func == 'All':
        plt.plot(x, sqr(x), 'blue')

    plt.show()
