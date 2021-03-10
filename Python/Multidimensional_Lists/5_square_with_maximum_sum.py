def create_matrix():
    matrix = list()
    (user_rows, user_columns) = [int(element) for element in input().split(', ')]
    for _ in range(user_rows):
        matrix.append([int(element) for element in input().split(', ')])
    return matrix


def get_sub_sum(matrix, row, col):
    return matrix[row][col] + matrix[row][col + 1] + \
           matrix[row + 1][col] + matrix[row + 1][col + 1]


def print_submatrix(matrix, row, col):
    for r in range(row, row + 2):
        for c in range(col, col + 2):
            print(matrix[r][c], end=" ")
        print()


matrix = create_matrix()
best_position = (0, 0)
best_value = get_sub_sum(matrix, 0, 0)

for row in range(len(matrix) - 1):
    for col in range(len(matrix[row]) - 1):
        current_value = get_sub_sum(matrix, row, col)
        if best_value < current_value:
            best_value = current_value
            best_position = (row, col)


(best_row, best_col) = best_position
print_submatrix(matrix, best_row, best_col)
print(best_value)