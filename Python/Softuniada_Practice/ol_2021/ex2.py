number = int(input())

for row_index in range(number):
    print(row_index * ' ', end='')

    for n in range(1, number - row_index + 1):
        print(n, end='')

    for n in range(number - row_index - 1, 0s, -1) :
        print(n, end='')

    print()
