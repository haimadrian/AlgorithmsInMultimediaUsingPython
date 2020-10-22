# ID
__author__ = "Haim Adrian"

import numpy as np
from numbers import Number


def DigitInMat(thickness):
    # thickness must be a positive integer
    if thickness is None or not isinstance(thickness, Number) or thickness != np.int64(thickness) or thickness <= 0:
        return None

    thickness = np.int64(thickness)
    mat = np.zeros((7 * thickness, 5 * thickness), dtype=np.uint8)
    Dim = mat.shape

    # Paint the horizontal part of the number 7
    mat[thickness: thickness * 2, thickness: Dim[1] - thickness] = 1

    # Paint the vertical part of the number 7
    mat[thickness: Dim[0] - thickness, Dim[1] - thickness * 2: Dim[1] - thickness] = 1

    return mat
