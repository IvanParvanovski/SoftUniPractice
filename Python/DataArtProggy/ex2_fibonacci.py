def calc_fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]

    sequence = [0, 1]

    for _ in range(n):
        a = sequence[-1]
        b = sequence[-2]

        sequence.append(a + b)

    return sequence


n = int(input())
print(calc_fibonacci(n))
