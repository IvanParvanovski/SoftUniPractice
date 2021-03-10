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


def print_matrix(matrix):
    return [print(''.join(row)) for row in matrix]


def is_new_row_valid(row, matrix):
    if -1 < row < len(matrix):
        return True
    return False


def is_new_column_valid(column, matrix):
    if -1 < column < len(matrix):
        return True
    return False


commands = {"up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1), }

text = input()
field_size = int(input())
matrix = create_matrix(field_size)
starting_row, starting_col = find_starting_point(matrix)
command_count = int(input())

for _ in range(command_count):
    command = input()
    if command in commands:
        position_changes = commands[command]
        new_position = (starting_row + position_changes[0], starting_col + position_changes[1])
        new_row = new_position[0]
        new_column = new_position[1]
        if is_new_row_valid(new_row, matrix) and is_new_column_valid(new_column, matrix):
            element = matrix[new_row][new_column]
            if element != '-':
                text += element
            matrix[new_row][new_column] = 'P'
            matrix[starting_row][starting_col] = '-'
            starting_row, starting_col = new_row, new_column
        else:
            text = text[:-1:]


print(text)
print_matrix(matrix)