num = int(input())
counter = 0

for x1 in range(num + 1):
    for x2 in range(num + 1):
        for x3 in range(num + 1):
            if x1 + x2 + x3 == num:
                counter += 1

print(counter)