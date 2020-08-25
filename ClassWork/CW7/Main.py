__author__ = "Haim Adrian"

import os
from Functions import *
from matplotlib import pyplot as plt


def ex1():
    file_data = readExcelToMatrix(os.path.join('KNNData', 'Data1.xlsx'))
    data = file_data[:, 0: 3].copy()
    new_samples = file_data[:, 3: 6].copy()
    new_samples = myKNN(5, data, new_samples)

    x0, y0 = zip(data[:, 1:3][data[:, 0] == 0].transpose())
    x1, y1 = zip(data[:, 1:3][data[:, 0] == 1].transpose())
    x2, y2 = zip(data[:, 1:3][data[:, 0] == 2].transpose())

    new_x0, new_y0 = zip(new_samples[:, 1:3][new_samples[:, 0] == 0].transpose())
    new_x1, new_y1 = zip(new_samples[:, 1:3][new_samples[:, 0] == 1].transpose())
    new_x2, new_y2 = zip(new_samples[:, 1:3][new_samples[:, 0] == 2].transpose())

    plt.figure('Assignment 1')
    plt.plot(x0, y0, 'ro')
    plt.plot(x1, y1, 'go')
    plt.plot(x2, y2, 'bo')
    plt.plot(new_x0, new_y0, 'r*')
    plt.plot(new_x1, new_y1, 'g*')
    plt.plot(new_x2, new_y2, 'b*')
    plt.title('0 = Original,  * = New')
    plt.subplots_adjust(0.05, 0.05, 0.95, 0.95, 0.1, 0.1)
    plt.show()


def ex2():
    file_data = readExcelToMatrix(os.path.join('KMeansData', 'Data1.xlsx'))
    data = file_data[:, 0: 2].copy()
    result = myKMeans(5, data)


ex1()
