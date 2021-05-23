import math

circle_perimeter = int(input())
radius_of_circle = float(input())
result = list()

for a in range(circle_perimeter // 2):
    for b in range(circle_perimeter // 2):
        for c in range(circle_perimeter // 2):
            if a == 0 and b == 0 and c == 0:
                continue

            if a + b + c == circle_perimeter and max(a, b, c) == radius_of_circle * 2:
                result.append((a, b, c))

for r in sorted(result, reverse=True):
    output = ''
    for letter in r:
        output += '{' + f'{letter}' + '}.'
    print(output[:-1])
