# ID
__author__ = "Haim Adrian"


def InverseDictionary(dic):
    if dic is None or not isinstance(dic, dict):
        return None

    # A helper dictionary to count keys, so we can use the updated count of each key
    countsDic = {}

    # The result dictionary (reverse)
    reverseDic = {}

    for k, v in dic.items():
        count = 0

        # In case value was already visited, get the count we kept
        if v in countsDic:
            count = countsDic[v]

        # Keep the count for next time we encounter this value
        countsDic[v] = count + 1
        reverseDic[(v, count)] = k

    return reverseDic
