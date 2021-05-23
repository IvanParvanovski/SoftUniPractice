def full_loop():
    evens = list()
    for i in range(10):
        if i % 2 == 0:
            evens.append(i)
    return evens


comprehension = [x for x in range(10) if x % 2 == 0]

print(full_loop())
print(comprehension)
