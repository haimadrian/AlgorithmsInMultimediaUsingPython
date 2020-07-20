from random import randrange


def maxOfThree(a, b, c):
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    elif b >= c:
        return b
    else:
        return c

