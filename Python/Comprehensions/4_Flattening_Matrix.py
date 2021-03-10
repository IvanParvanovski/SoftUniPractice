matrix_rows = int(input())
matrix = [list(map(int, input().split(', '))) for _ in range(matrix_rows)]
flattening_matrix = [num for sublist in matrix for num in sublist]
print(flattening_matrix)
