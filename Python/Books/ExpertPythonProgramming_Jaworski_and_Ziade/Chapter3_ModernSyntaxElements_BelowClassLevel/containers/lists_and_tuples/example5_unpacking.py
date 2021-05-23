# unpacking
first, second, third = 'foo', 'bar', 100

print(first)
print(second)
print(third)
print()

# starred expression to capture rest of the sequence
first, second, *rest = 1, 2, 3, 4

print(first)
print(second)
print(rest)
print()

# starred expression to capture middle of the sequence
first, *inner, last = 0, 1, 2, 3

print(first)
print(*inner)
print(last)
print()

# nested unpacking
(a, b), (c, d) = (1, 2), (3, 4)
print(a, b, c, d)

a, b, c, d = (1, 2), (3, 4)
print(a, b, c, d)
