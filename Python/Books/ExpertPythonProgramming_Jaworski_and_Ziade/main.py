from collections import defaultdict

matrix = [
    [1, 2, 3],
    [4, 5, 1],
    [5, 5, 3],
]

col_dict = defaultdict(int)

for row in matrix:
    for index, col in enumerate(row):
        col_dict[index] += col

sorted_col_dict = sorted(col_dict.items(), key=lambda x: x[1])

for row in matrix:
    for result in sorted_col_dict:
        print(row[result[0]], end=" ")
    print()
