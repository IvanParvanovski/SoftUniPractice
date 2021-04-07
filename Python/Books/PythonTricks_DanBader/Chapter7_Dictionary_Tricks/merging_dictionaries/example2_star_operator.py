xs = {'a': 1, 'b': 2}
ys = {'b': 3, 'c': 4}

zs = dict(xs, **ys)
print(zs)
