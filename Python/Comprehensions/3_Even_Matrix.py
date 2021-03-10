matrix_rows = int(input())
matrix = [list(map(int, input().split(', '))) for _ in range(matrix_rows)]
matrix = [[num for num in numbers if num % 2 == 0] for numbers in matrix]
print(matrix)