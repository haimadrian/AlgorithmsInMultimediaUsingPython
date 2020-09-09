__author__ = "Haim Adrian"

from functions import *
from matplotlib import pyplot as plt


def main():
    X = np.arange(0, 101)
    Y = [func(x) for x in X]

    plt.figure('Assignment 1')
    plt.plot(X, Y, 'r')
    plt.pause(0.05)
    plt.title('(sin(x) + 0.25 * |x - 30|) * (x - 50)^2')
    plt.xlabel('X (1kHz)')
    plt.ylabel('Y')

    prev_point = np.random.randint(0, len(X))
    epsilon = 1
    gamma = 1e-2
    while True:
        dfdx = func(prev_point + 2) - func(prev_point)
        curr_point = int(np.floor(prev_point - gamma * dfdx))
        plt.plot(curr_point, func(curr_point), 'bo')
        plt.pause(0.05)
        if np.abs(dfdx) < epsilon:
            print(dfdx)
            break
        new_dfdx = func(curr_point + 1) - func(curr_point)
        if new_dfdx == dfdx:
            print('equals:', dfdx)
            break
        gamma = (curr_point - prev_point) / np.abs(new_dfdx - dfdx)
        prev_point = curr_point
    plt.show()


main()
