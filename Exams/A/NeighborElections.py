# ID
__author__ = "Haim Adrian"

import numpy as np


def NeighborElections(nearest_neighbors_labels, distances):
    """
    Returns the selected label from the nearest_neighbors_labels.

    Parameters
    ----------
    nearest_neighbors_labels : np.ndarray
        One dimensional array.
        Each element in the array represent a sample label. The array sorted by distances, from smallest to largest.
    distances : np.ndarray
        One dimensional array.
        The shape of the array is equal to nearest_neighbors_labels shape. Each element in the array represents
        the distance between the new sample and the labeled sample in a matching index in nearest_neighbors_labels.
        The array sorted from smallest to largest.

    Returns
    -------
    out: nearest_neighbors_labels.dtype
        The return value is scalar, represent the chosen label.
    """
    unique, counts = np.unique(nearest_neighbors_labels, return_counts=True)
    maxAppearances = np.max(counts)
    if len(counts[counts == maxAppearances]) == 1:
        return unique[np.argmax(counts)]
    else:
        # Repeat the process until we find max count
        k = len(nearest_neighbors_labels) - 1
        while k > 0:
            unique, counts = np.unique(nearest_neighbors_labels[: k], return_counts=True)
            maxAppearances = np.max(counts)

            if len(counts[counts == maxAppearances]) == 1:
                return unique[np.argmax(counts)]

            k = k-1

        return None
