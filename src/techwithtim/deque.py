# 8 collections deque

from collections import deque
import pprint

d = deque("hello")
print(d)
l = list("hello")
print(l)


d.append("4")
print(d)
d.append(5)
print(d)
d.appendleft(1)
print(d)

val = d.pop()
pprint.pprint(val)
pprint.pprint(d)

# d.clear()
print(d)


d.extend("456")
d.extendleft([1, 2, 3])
# note extend left adds in reverse order

print(d)
d = deque("123456789")
print(d)
d.rotate(-5)
print(d)


d = deque("hello", maxlen=5)
print(d)
d.append(1)
print(d)
d.appendleft("h")
print(d)

d.reverse()
print(d)
