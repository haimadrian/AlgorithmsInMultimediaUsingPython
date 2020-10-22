__author__ = "Haim Adrian"

from functions import *
from matplotlib import pyplot as plt


def gradient_descent():
    dx = 1e-3
    X = np.arange(0, 100, dx)
    Y = func(X)

    plt.figure('Assignment 1')
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.plot(X, Y)
    plt.grid()
    plt.xlabel('X (1kHz)')
    plt.ylabel('Y')
    plt.pause(1/24)

    myGradientDescent(func, dx)

    plt.show()


gradient_descent()
