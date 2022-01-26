print(map(lambda x: x ** 2, range(10)))
print(list(map(lambda x: x ** 2, range(10))))

list(map(print, range(5), range(4), range(6)))


def sum(a, b):
    return a + b


# list 1
lst1 = [2, 4, 6, 8]

# list 2
lst2 = [1, 3, 5, 7, 9]

result = list(map(sum, lst1, lst2))
print(result)
