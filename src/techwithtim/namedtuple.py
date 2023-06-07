# 7 namedtuple

from collections import namedtuple
import pprint

Point = namedtuple("Point", "x y z")

newP = Point(3, 4, 5)

print(newP)
pprint.pprint(newP)


Point1 = namedtuple("Point", ["x", "y", "l"])
newP = Point1(3, 4, 5)
print(newP)


Point1 = namedtuple("Point", {"x": 0, "y": 1, "l": 2})

newP = Point1(3, 4, 5)
print(newP)


newP = Point(3, 4, 5)
print("💥", newP.x, newP.y, newP.z)
print(newP._fields)
newPP = newP._replace(y=6)
print(newPP)

p2 = Point._make(["a", "b", "c"])
print(p2)
