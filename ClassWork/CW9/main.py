__author__ = "Haim Adrian"

from functions import *
from matplotlib import pyplot as plt


def main():
    X = np.arange(0, 100, 1/1000)
    Y = np.array([func(x) for x in X])

    plt.figure('Assignment 1')
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.plot(X, Y, 'r')
    plt.title('(sin(x) + 0.25 * |x - 30|) * (x - 50)^2')
    plt.grid()
    plt.xlabel('X (1kHz)')
    plt.ylabel('Y')

    prev_point = np.random.uniform(80, 90)
    curr_point = prev_point + 0.01
    xs = curr_point

    plt.plot(xs, Y[np.argmin(np.abs(X - xs))], 'bx')

    df = np.gradient(Y)

    epsilon = 1e-7
    while True:
        df0 = df[np.argmin(np.abs(X - prev_point))]
        df1 = df[np.argmin(np.abs(X - curr_point))]

        eps = (df1 - df0) ** 2
        if eps <= epsilon:
            break

        # Avoid division by zero
        if eps:
            # t = (x1 - x0) * (df1 - df0) / ((df1 - df0) ** 2)
            # In case of 1 dimension, the equation can be shortened:
            gamma = (curr_point - prev_point) / (df1 - df0)
        else:
            gamma = 0
            prev_point = curr_point

        prev_point, curr_point = curr_point, prev_point - (np.abs(gamma) * df0)
        # Gradient Ascent would be calculated as: x0 + (np.abs(t) * df0)

        # Avoid going out of boundaries
        if curr_point < X[0]:
            curr_point = X[0]
            break
        elif curr_point > X[-1]:
            curr_point = X[-1]
            break

        # Dynamic graph
        plt.plot(curr_point, Y[np.argmin(np.abs(X - curr_point))], 'bo')
        # plt.grid()
        plt.pause(0.5)
        # plt.cla()
    print('Finish')
    plt.plot(curr_point, Y[np.argmin(np.abs(X - curr_point))], 'r*')
    plt.pause(0.5)
    plt.show()


main()
