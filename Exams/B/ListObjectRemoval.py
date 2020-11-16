# 305265514
__author__ = "Haim Adrian"

from numbers import Number


def ListObjectRemoval(myList):
    # For None or not-a-list, just return what we've received
    if myList is not None and isinstance(myList, list):
        for item in myList:
            if not isinstance(item, Number):
                myList.remove(item)

    return myList
