from functools import reduce
print(reduce(lambda a, b: a + b, [2, 2]))
print(reduce(lambda a, b: a + b, [2, 2, 2]))
print(reduce(lambda a, b: a + b, range(100)))
