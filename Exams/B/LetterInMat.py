# 305265514
__author__ = "Haim Adrian"

import numpy as np
from numbers import Number


def LetterInMat(thickness):
    # thickness must be a positive integer
    if thickness is None or not isinstance(thickness, Number) or thickness != np.int64(thickness) or thickness <= 0:
        return None

    thickness = np.int64(thickness)
    mat = np.ones((6 * thickness, 5 * thickness), dtype=np.uint8)
    dim = mat.shape

    # Paint the horizontal parts of the letter C
    mat[list(range(thickness, thickness * 2)) + list(range(dim[0] - thickness * 2, dim[0] - thickness)), thickness: dim[1] - thickness] = 0

    # Paint the vertical part of the letter C, considering we've already painted some of the area while painting the horizontal parts
    mat[thickness * 2: dim[0] - thickness * 2, thickness: thickness * 2] = 0

    return mat
