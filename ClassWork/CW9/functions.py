__author__ = "Haim Adrian"

import numpy as np


def func(x):
    y = (np.sin(x) + 0.25*np.abs(x - 30)) * ((x - 50) ** 2)
    return y
