def create_matrix(rows_count, columns_count):
    matrix = list()
    for _ in range(rows_count):
        matrix.append(list(int(x) for x in input().split()))
    return calculate_matrix_sum(matrix, columns_count)


def calculate_matrix_sum(matrix, columns_count):
    matrix_columns_sum = [0] * columns_count
    for element in matrix:
        for index in range(len(element)):
            matrix_columns_sum[index] += element[index]
    return matrix_columns_sum


(rows, columns) = list([int(x) for x in input().split(', ')])

[print(x) for x in create_matrix(rows, columns)]
