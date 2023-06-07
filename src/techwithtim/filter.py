# 4 filter function
from icecream import ic


def add7(x):
    return x + 7


def isOdd(x):
    return x % 2 != 0


a = [x for x in range(11) if x != 0]
ic(a)
b = list(filter(isOdd, a))
ic(b)

c = list(map(add7, b))
ic(c)
