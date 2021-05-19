for items in zip([1, 2, 3], [4, 5, 6]):
    print(items)


# zip(...)
# 1, 4
# 2, 5
# 3, 6


# zip(*zip(...))
# 1, 2, 3
# 4, 5, 6


for items in zip(*zip([1, 2, 3], [4, 5, 6])):
    print(items)

for items in zip([1, 2, 3, 4], [1, 2]):
    print(items)

