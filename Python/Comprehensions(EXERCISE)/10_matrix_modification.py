rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
while True:
    raw_input = input().split()
    if raw_input[0] == "END":
        break

    command = raw_input[0]
    row_index = int(raw_input[1])
    col_index = int(raw_input[2])
    value = int(raw_input[3])

    if len(matrix) > row_index > -1 and len(matrix[row_index]) > col_index > -1:
        if command == "Add":
            matrix[row_index][col_index] += value
        elif command == "Subtract":
            matrix[row_index][col_index] -= value
    else:
        print("Invalid coordinates")

[print(' '.join(map(str, numbers))) for numbers in matrix]