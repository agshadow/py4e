# 6 Collections

import collections
from collections import Counter

# Containers
# list
# set
# dict
# tuple


# Types:
# 1 counter
# 2 deque
# 3 namedTuple()
# 4 orderedDict
# 5 defaultdict

c = Counter("gallad")
print(c)
c = Counter(["a", "a", "b", "c", "c"])
print(f"{c=}")
c = Counter({"a": 1, "b": 2})

print(c)
c = Counter(cats=4, dogs=7)
print(c)
print(f'{c["cats"]=}')
print(f'{c["birds"]=}')

print(list(c.elements()))

print(c.most_common(1)[0][1])
dogs = ("dogs", 7)
print(dogs)

c = Counter(["a", "a", "b", "c", "c"])
d = ["a", "b", "b", "c"]
print(c.subtract(d))
print(c)

c.update(d)
print(c)

c.clear()
print(c)

c = Counter(["a", "a", "b", "c", "c"])
d = Counter(["a", "b", "b", "c"])
print(f"{c=}")
print(f"{d=}")
e = c + d
print(e)

e = c - d
print(e)

c = Counter(["a", "a", "b", "c", "c"])
d = Counter(["a", "b", "b", "c"])
# intersection
print(c & d)
