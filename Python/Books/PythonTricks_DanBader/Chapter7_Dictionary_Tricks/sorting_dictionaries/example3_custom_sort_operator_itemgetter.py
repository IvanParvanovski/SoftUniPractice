import operator

xs = {'a': 1, 'c': 2, 'b': 3, 'd': 1}
print(sorted(xs.items(), key=operator.itemgetter(1)))
