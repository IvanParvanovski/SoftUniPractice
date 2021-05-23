def rindex(lst, value):
    lst.reverse()
    i = lst.index(value)
    lst.reverse()
    return len(lst) - i - 1


row_count, col_count = map(int, input().split())
matrix = list()

for r in range(row_count):
    matrix.append(input().split())

egg_found_symbol = input()
start_row_index, start_col_index = map(int, input().split())

start_symbol = matrix[start_row_index][start_col_index]
matrix[start_row_index][start_col_index] = egg_found_symbol

directions = {
    'up': lambda row, col: (row - 1, col),
    'down': lambda row, col: (row + 1, col),
    'left': lambda row, col: (row, col - 1),
    'right': lambda row, col: (row, col + 1),
}

can_change = True
while True:
    if not can_change:
        break

    can_change = False
    for row_index, row in enumerate(matrix):
        if egg_found_symbol in row:
            first_symbol_col = row.index(egg_found_symbol)
            last_symbol_col = rindex(row, egg_found_symbol)

            for current_symbol_col in range(first_symbol_col, last_symbol_col + 1):

                for col_index in range(current_symbol_col + 1, len(row)):
                    if matrix[row_index][col_index] != start_symbol:
                        break

                    can_change = True
                    matrix[row_index][col_index] = egg_found_symbol

                for col_index in range(current_symbol_col - 1, -1, -1):
                    if matrix[row_index][col_index] != start_symbol:
                        break

                    can_change = True
                    matrix[row_index][col_index] = egg_found_symbol

                for current_row_index in range(row_index + 1, len(matrix)):
                    if matrix[current_row_index][current_symbol_col] != start_symbol:
                        break

                    can_change = True
                    matrix[current_row_index][current_symbol_col] = egg_found_symbol

                for current_row_index in range(row_index - 1, -1, -1):
                    if matrix[current_row_index][current_symbol_col] != start_symbol:
                        break

                    can_change = True
                    matrix[current_row_index][current_symbol_col] = egg_found_symbol

for r in matrix:
    print(''.join(r))
