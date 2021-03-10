def create_matrix(size):
    local_matrix = list()
    for _ in range(size):
        local_matrix.append(list(input()))
    return local_matrix


def find_starting_point(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            element = matrix[row][col]
            if element == 'P':
                return row, col


def move_down(row, matrix, word):
    row += 1
    if row >= len(matrix):
        row -= 1
        word = word[:len(word) - 1:]
    return row, word


def move_up(row, word):
    row -= 1
    if row < 0:
        row += 1
        word = word[:len(word) - 1:]
    return row, word


def move_left(col, word):
    col -= 1
    if col < 0:
        col += 1
        word = word[:len(word) - 1:]
    return col, word


def move_right(col, matrix, word):
    col += 1
    if col >= len(matrix):
        col -= 1
        word = word[:len(word) - 1:]
    return col, word


def print_matrix(matrix):
    return [print(''.join(row)) for row in matrix]


commands = {"up",
            "down",
            "left",
            "right", }

text = input()
field_size = int(input())
matrix = create_matrix(field_size)
starting_row, starting_col = find_starting_point(matrix)
command_count = int(input())

for _ in range(command_count):
    command = input()
    if command in commands:
        matrix[starting_row][starting_col] = '-'
        if command == "up":
            starting_row, text = move_up(starting_row, text)

        elif command == "down":
            starting_row, text = move_down(starting_row, matrix, text)

        elif command == "left":
            starting_col, text = move_left(starting_col, text)

        elif command == "right":
            starting_col, text = move_right(starting_col, matrix, text)

        element = matrix[starting_row][starting_col]
        if element != '-':
            text += element
        matrix[starting_row][starting_col] = 'P'

print(text)
print_matrix(matrix)