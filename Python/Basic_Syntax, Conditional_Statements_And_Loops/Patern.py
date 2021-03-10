input_number = int(input())

for columns1 in range(1, input_number + 1):
    for rows in range(1, columns1 + 1):
        print("*" , end="")
    print()

for columns2 in range(input_number - 1, 0, - 1):
    for rows2 in range(columns2 + 1, 1, - 1):
        print("*", end="")
    print()