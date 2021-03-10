(rows_count, columns_count) = input().split(', ')

matrix = list()
matrix_sum = 0

for row in range(int(rows_count)):
    matrix.append(list(int(x) for x in input().split(', ')))
    matrix_sum += sum(matrix[row])

print(matrix_sum)
print(matrix)
