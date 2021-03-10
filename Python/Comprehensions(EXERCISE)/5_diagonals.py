rows_count = int(input())
matrix = [list(map(int, input().split(', '))) for _ in range(rows_count)]


first_diagonal = [matrix[i][i] for i in range(rows_count)]
second_diagonal = [matrix[i][rows_count - 1 - i] for i in range(rows_count)]

print(f"First diagonal: {', '.join(map(str, first_diagonal))}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join(map(str, second_diagonal))}. Sum: {sum(second_diagonal)}")
