__author__ = "Haim Adrian"

import numpy as np
from matplotlib import pyplot as plt


def func(x):
    y = (np.sin(x) + 0.25*np.abs(x - 30)) * ((x - 50) ** 2)
    return y


def gradientFunc(function, x, dx):
    Xs = np.array([x - dx, x, x + dx], dtype=np.float64)
    Y = function(Xs)
    dydx = np.gradient(Y, dx)
    return dydx[1]


def gamma(x0, x1, df0, df1):
    if np.abs(df1 - df0) < 1e-10:
        return 1e-2

    gamma1 = np.abs((x1 - x0) / (df1 - df0))
    return gamma1


def myGradientDescent(function, dx, epsilon=1e-1):
    # Starting X between 0 to 100
    starting_x = np.random.rand()*100
    plt.plot(starting_x, function(starting_x), 'gs')
    plt.pause(1/24)

    new_x = current_x = starting_x
    new_df = current_df = gradientFunc(function, current_x, dx)
    iteration_num = 0

    flag = True
    while flag:
        iteration_num += 1
        new_x = current_x - gamma(current_x, new_x, current_df, new_df) * current_df
        new_df = gradientFunc(function, new_x, dx)
        y = function(new_x)
        print('f({0:.2f}) = {1:.5f}'.format(new_x, y))
        print('df({0:.2f}) = {1:.5f}\n'.format(new_x, new_df))

        if (new_df - current_df)**2 < epsilon:
            flag = False
            plt.plot(new_x, y, 'b*')
        else:
            current_x = new_x
            current_df = new_df
            plt.plot(new_x, y, 'ro')

        plt.title('StartingX={:.2f}, Iteration={}, f({:.2f}) = {:.5f}'.format(starting_x, iteration_num, new_x, y))
        plt.pause(2/24)

    print('Starting X: ', starting_x)
    print('Iteration: ', iteration_num)
