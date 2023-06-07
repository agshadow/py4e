li = [x for x in range(11) if x > 0]
print(li)


def func(x):
    return x**x


print(list(map(func, li)))

print([func(x) for x in li if x % 2])
