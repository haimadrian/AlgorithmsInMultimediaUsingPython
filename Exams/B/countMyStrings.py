# 305265514
__author__ = "Haim Adrian"


# 24-05-2019 exam.
def countMyStrings(string):
    if string is None or not isinstance(string, str):
        return None

    # First, lowercase the string so we will count characters ignoring case
    string = string.lower()

    # Second, make the characters of a string into set so we will count each character without repeating ourselves
    counts = {c: string.count(c) for c in set(string)}

    return counts
