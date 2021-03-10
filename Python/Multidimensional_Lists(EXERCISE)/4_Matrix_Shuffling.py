def create_matrix(lines_count):
    return [input().split() for _ in range(lines_count)]


def print_matrix(matrix):
    for elements_list in matrix:
        for element in elements_list:
            print(element, end=" ")
        print()


(matrix_rows, matrix_columns) = list(int(x) for x in input().split())
matrix = create_matrix(matrix_rows)

while True:
    raw_input = input().split()
    command = raw_input[0]

    if command == "END":
        break

    elif command == "swap":
        if len(raw_input) == 5:
            first_row_index = int(raw_input[1])
            second_row_index = int(raw_input[3])
            row_check_bigger = first_row_index < matrix_rows and second_row_index < matrix_rows
            row_check_smaller = first_row_index >= 0 and second_row_index >= 0

            first_column_index = int(raw_input[2])
            second_column_index = int(raw_input[4])
            col_check_bigger = first_column_index < matrix_columns and second_column_index < matrix_columns
            col_check_smaller = first_column_index >= 0 and second_column_index >= 0

            if row_check_bigger and row_check_smaller and col_check_bigger and col_check_smaller:
                first_row = matrix[first_row_index]
                second_row = matrix[second_row_index]

                first_row[first_column_index], second_row[second_column_index] = second_row[second_column_index], first_row[first_column_index]
                print_matrix(matrix)

            else:
                print("Invalid input!")
        else:
            print("Invalid input!")

    else:
        print("Invalid input!")
