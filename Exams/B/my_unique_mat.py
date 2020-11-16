# 305265514
__author__ = "Haim Adrian"

import numpy as np


def my_unique_mat(size):
    if size != np.uint64(size):
        return None

    myMat, myMat[np.eye(size) == 1], myMat[np.eye(size)[::-1] == 1], myMat[int(np.round(size / 2 - 0.5)), int(np.round(size / 2 - 0.5))] = np.ones((size, size), dtype=np.uint8), 0, 2, (1 if size % 2 == 1 else 0)

    return myMat
