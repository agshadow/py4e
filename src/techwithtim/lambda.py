# 5 Lambda Tutorial
from icecream import ic


def func(x):
    func2 = lambda x: x + 5
    return func2(x) + 85


func3 = lambda x, y=10: x + y

print(func3(5, 5))
print(func3(5))

ic(func(2))

a = list(x for x in range(11) if x > 0)
print(a)

newList = list(map(lambda x: x + 5, a))

ic(newList)

newList = list(filter(lambda x: x % 2 == 0, a))
print(f"{newList=}")
