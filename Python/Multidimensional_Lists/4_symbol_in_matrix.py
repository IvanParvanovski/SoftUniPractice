def create_matrix(rows_count):
    matrix = list()
    for _ in range(rows_count):
        matrix.append([ord(char) for char in list(input())])
    return matrix


def find_symbol(matrix):
    symbol = input()
    check = False
    special_numbers = list()
    for numbers_index in range(len(matrix)):
        matrix_number_index = matrix[numbers_index]

        for num_index in range(len(matrix_number_index)):
            if ord(symbol) == matrix_number_index[num_index]:
                check = True
                special_numbers.extend([str(numbers_index), str(num_index)])
                break

        if check:
            break

    if check:
        (numbers_index, num_index) = special_numbers
        print(f"({numbers_index}, {num_index})")

    else:
        print(f"{symbol} does not occur in the matrix ")


matrix = create_matrix(int(input()))
find_symbol(matrix)
