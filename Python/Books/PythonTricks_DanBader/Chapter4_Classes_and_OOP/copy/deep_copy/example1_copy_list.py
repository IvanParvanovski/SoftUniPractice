from copy import deepcopy
xs = [
    [1, 2, 3],
    [4, 5, 6],
]

ys = deepcopy(xs)

print(xs)
print(ys)

xs.append(['hello'])
print()
print(xs)
print(ys)

xs[0][1] = 'X'
print()
print(xs)
print(ys)
