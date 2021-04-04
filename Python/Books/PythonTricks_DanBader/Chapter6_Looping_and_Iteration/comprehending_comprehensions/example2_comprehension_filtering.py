even_squares = [x * x for x in range(10) if x % 2 == 0]
print(even_squares)

even_squares2 = list()

for x in range(10):
    if x % 2 == 0:
        even_squares2.append(x * x)

print(even_squares2)