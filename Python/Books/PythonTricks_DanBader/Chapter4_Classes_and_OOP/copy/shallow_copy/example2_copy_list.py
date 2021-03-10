from copy import copy
xs = [[1, 2, 3], [4, 5, 6]]
ys = copy(xs)

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
