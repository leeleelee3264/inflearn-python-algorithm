def rotLeft(a, d):
    if d > len(a):
        d = d % len(a)
    return a[d:] + a[:d], d


def getMaxElementIndexes(a, rotate):
    # Write your code here
    res = []

    m = a.index(max(a))

    for i in rotate:
        _a, _d = rotLeft(a, i)

        if _d == len(a):
            _m = m
        elif m >= _d:
            _m = m - _d
        else:
            _m = m + (_d - m)

        res.append(_m)

    return res


print(getMaxElementIndexes([1,2,3], [1,2,3,4]))