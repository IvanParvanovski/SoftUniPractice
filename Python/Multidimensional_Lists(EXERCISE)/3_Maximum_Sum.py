def create_matrix(lines_count):
    return [list(map(int, input().split())) for _ in range(lines_count)]


def find_the_3x3_biggest_sum(rows, columns, matrix):
    the_best_sum = 0
    the_best_index = (0, 0)
    for row in range(rows - 2):
        for col in range(columns - 2):
            small_matrix_sum = 0
            for small_matrix_row in range(row, row + 3):
                for small_matrix_col in range(col, col + 3):
                    small_matrix_sum += matrix[small_matrix_row][small_matrix_col]
                    if small_matrix_sum > the_best_sum:
                        the_best_index = (row, col)
                        the_best_sum = small_matrix_sum

    return the_best_sum, the_best_index


def print_the_best_sum_elements(rows, columns, matrix):
    for row in range(rows, rows + 3):
        for col in range(columns, columns + 3):
            print(matrix[row][col], end=" ")
        print()


(user_rows, user_columns) = (int(x) for x in input().split())
matrix = create_matrix(user_rows)

the_best_sum, the_best_index = find_the_3x3_biggest_sum(user_rows, user_columns, matrix)
print(f"Sum = {the_best_sum}")
the_best_sum_row, the_best_sum_col = the_best_index

print_the_best_sum_elements(the_best_sum_row, the_best_sum_col, matrix)

