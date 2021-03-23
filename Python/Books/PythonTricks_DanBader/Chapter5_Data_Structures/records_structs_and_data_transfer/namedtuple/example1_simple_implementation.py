from collections import namedtuple
from sys import getsizeof

p1 = namedtuple('Point', 'x y z',)(1, 2, 3)
p2 = (1, 2, 3)

print(getsizeof(p1))
print(getsizeof(p2))
