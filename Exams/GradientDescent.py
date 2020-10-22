__author__ = "Haim Adrian"

from matplotlib import pyplot as plt
import numpy as np
import cv2
from numbers import Number


# Gradient Descent
def myGradDescent(sensitivity=10 ** (-7)):

    # Function Definition
    x = np.arange(0, 100, 0.001)
    fx = (np.sin(x) + 0.25 * np.abs(x - 30)) * (x - 50) ** 2

    # Random starting point
    x0 = np.random.uniform(0, 100)
    x1 = x0 + 0.01
    xs = x1

    # Gradient
    df = np.gradient(fx)
    dff = np.gradient(df)

    df0 = df[np.argmin(np.abs(x - x0))]
    df1 = df[np.argmin(np.abs(x - x1))]
    eps = (df1 - df0) ** 2

    # Descent loop
    plt.figure()
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.plot(x, fx)
    plt.plot(xs, fx[np.argmin(np.abs(x - xs))], 'gx')
    plt.grid()
    while eps > sensitivity:

        df0 = df[np.argmin(np.abs(x - x0))]
        df1 = df[np.argmin(np.abs(x - x1))]
        eps = (df1 - df0) ** 2

        # Avoid division by zero
        if eps:
            # t = (x1 - x0) * (df1 - df0) / ((df1 - df0) ** 2)
            # In case of 1 dimension, the equation can be shortened:
            t = (x1 - x0) / (df1 - df0)
        else:

            t = 0
            x0 = x1

        x0, x1 = x1, x0 - (np.abs(t) * df0)
        # Gradient Ascent would be calculated as: x0 + (np.abs(t) * df0)

        # Avoid going out of boundaries
        if x1 < x[0]:
            x1 = x0
            eps = -1
        elif x1 > x[-1]:
            x1 = x0
            eps = -1

        # Dynamic graph
        plt.plot(x1, fx[np.argmin(np.abs(x - x1))], 'ro')
        plt.pause(0.2)
        # plt.cla()
    plt.title('Done')
    # plt.plot(x, fx)
    plt.plot(xs, fx[np.argmin(np.abs(x - xs))], 'gx')
    plt.plot(x1, fx[np.argmin(np.abs(x - x1))], 'bo')
    # plt.grid()
    plt.show()


myGradDescent(1e-20)
