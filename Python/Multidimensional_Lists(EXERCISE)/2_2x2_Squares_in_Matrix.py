def create_matrix(lines_count):
    return [input().split() for _ in range(lines_count)]


def find_element_squares(rows, columns, matrix):
    counter = 0
    for row in range(rows - 1):
        for col in range(columns - 1):
            top_left_element = matrix[row][col]
            top_right_element = matrix[row][col + 1]
            down_left_element = matrix[row + 1][col]
            down_right_element = matrix[row + 1][col + 1]
            if top_left_element == top_right_element == down_left_element == down_right_element:
                counter += 1
    return counter


(user_rows, user_columns) = [int(x) for x in input().split()]
matrix = create_matrix(user_rows)
print(find_element_squares(user_rows, user_columns, matrix))
