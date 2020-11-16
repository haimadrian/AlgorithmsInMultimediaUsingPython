# ID
__author__ = "Haim Adrian"

import numpy as np
from numbers import Number


def GetListStatistics(myList):
    if myList is None or not isinstance(myList, list):
        return None

    # helper method to flat a list recursively, collecting numbers only
    def flatList(lst_inner):
        flattened = []
        for item in lst_inner:
            if isinstance(item, Number):
                flattened.append(item)
            elif isinstance(item, list):
                flattened.extend(flatList(item))
        return flattened

    allNumbers = flatList(myList)

    if len(allNumbers) > 0:
        return np.mean(allNumbers)

    # If there was no number in the list, just return none.
    return None
