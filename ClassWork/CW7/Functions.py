__author__ = "Haim Adrian"


import numpy as np
import pandas as pd
from numbers import Number


def readExcelToMatrix(file_path):
    data_frame = pd.read_excel(file_path, sheet_name='Sheet1')
    return data_frame.values


def myKNN(k, Data, NewSamples):
    if not isinstance(k, Number):
        print('myKNN: Not a number. k must be a number. Was:', k.__class__)
        return None

    if not isinstance(Data, np.ndarray) or not isinstance(NewSamples, np.ndarray):
        print('myKNN: Not a tensor. Was: Data=', Data.__class__, ', NewSamples=', NewSamples.__class__)
        return None

    if Data.ndim != 2 or NewSamples.ndim != 2:
        print("myKNN: Not a matrix. Was: Data=", Data.shape, ', NewSamples=', NewSamples.shape)
        return None

    if Data.shape[1] < 3 or NewSamples.shape[1] < 2:
        print("myKNN: Unexpected column number. Data should be 3, New should be 2. Was: Data=", Data.shape[1],
              ', NewSamples=', NewSamples.shape[1])
        return None

    # Make sure we will not get out of bounds
    k = int(np.max([np.min([k, Data.shape[0]]), 1]))

    for i in range(NewSamples.shape[0]):
        # First, calculate the norm (Euclidean) - Use axis=1 to sum the columns in each row, according to the presentation.
        norm = np.sum((Data[:, 1:] - NewSamples[i, 1:])**2, axis=1)**0.5

        # Second, map each norm to its label, so we can sort the values and then pick up k nearest neighbors
        indexed_norm = [(norm[j], Data[j, 0]) for j in range(norm.shape[0])]

        # Third, sort the norm values, to pick up the nearest ones. Sort by the norm, at index 0. Index 1 is the label
        indexed_norm.sort(key=lambda x: x[0])

        # Fourth, group values by their label, so we can count them and take the highest value
        nearest_neighbors = indexed_norm[: k]
        values = sorted(set(map(lambda x: x[1], nearest_neighbors)))
        newlist = [([y[0] for y in nearest_neighbors if y[1] == x], x) for x in values]
        # For example: newlist = [([val1, val2], label1),  ([val3], label2),  ([val4, val5, val6], label3)]

        max_label = -1  # -1 indicates unknown
        max_length = 0
        count = 0
        for j in range(len(newlist)):
            if len(newlist[j][0]) > max_length:
                count = 1
                max_length = len(newlist[j][0])
                max_label = newlist[j][1]
            elif len(newlist[j][0]) == max_length:
                count += 1

        if count > 1:
            print('Found same amount of neighbors from', count, 'different labels. Choosing unknown label: -1')
            max_label = -1

        NewSamples[i, 0] = max_label

    return NewSamples


def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 0)
    vector[:pad_width[0]] = pad_value


def myKMeans(k, Data):
    if not isinstance(k, Number):
        print('myKMeans: Not a number. k must be a number. Was:', k.__class__)
        return None

    if not isinstance(Data, np.ndarray):
        print('myKMeans: Not a tensor. Was: Data=', Data.__class__)
        return None

    if Data.ndim != 2:
        print("myKMeans: Not a matrix. Was: Data=", Data.shape)
        return None

    if Data.shape[1] < 2:
        print("myKMeans: Unexpected column number. Data should be 2. Was: Data=", Data.shape[1])
        return None

    # Make sure we will not get out of bounds
    k = np.max([np.min([k, Data.shape[0]]), 1])

    # Pad the matrix from left, so we will have a column for labels
    labeled = np.pad(Data, (1, 0), pad_with, padder=0)

