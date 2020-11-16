# ID
__author__ = "Haim Adrian"

import numpy as np


def ChangeColors(img: np.ndarray):
    if img.ndim != 3:
        return None
    new_img = img.copy()
    new_img[:, :, 0][np.logical_or(new_img[:, :, 1] <= 60, new_img[:, :, 2] <= 60)] = new_img[:, :, 1][np.logical_or(new_img[:, :, 1] <= 60, new_img[:, :, 2] <= 60)] + 150
    return new_img
