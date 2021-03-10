def create_matrix(lines_count):
    return [list(map(int, input().split())) for _ in range(lines_count)]


def main_diagonal(matrix):
    main_diagonal_sum = 0
    n = len(matrix)
    for row in range(n):
        for col in range(n):
            if row == col:
                main_diagonal_sum += matrix[row][col]
    return main_diagonal_sum


def secondary_diagonal(matrix):
    secondary_diagonal_sum = 0
    n = len(matrix)
    for row in range(n):
        for col in range(n):
            if col == n - row - 1:
                secondary_diagonal_sum += matrix[row][col]
    return secondary_diagonal_sum


matrix = create_matrix(int(input()))
print(abs(main_diagonal(matrix) - secondary_diagonal(matrix)))

