def read_input(rows_count):
    read_matrix = list()

    for _ in range(rows_count):
        read_matrix.append(list(int(num) for num in input().split()))

    return read_matrix


matrix = read_input(int(input()))

main_line_sum = 0
for index in range(len(matrix)):
    main_line_sum += matrix[index][index]

print(main_line_sum)