def create_matrix(size):
    matrix = list()
    for index in range(size):
        matrix.append(input().split())
    return matrix


def find_starting_position(matrix):
    for index in range(len(matrix)):
        row = matrix[index]
        if 'p' in row:
            return index, row.index('p')


def transform_filed_right_left(row, column, new_column, command, killed_targets):
    if command == "move":
        if matrix[row][new_column] == '.':
            matrix[row][new_column] = 'p'
            matrix[row][column] = '.'
            return (row, new_column), killed_targets

    elif command == "shoot":
        matrix[row][new_column] = 'x'
        killed_targets += 1
    return (row, column), killed_targets


def transform_filed_up_down(row, column, new_row, command, killed_targets):
    if command == "move":
        if matrix[new_row][column] == '.':
            matrix[new_row][column] = 'p'
            matrix[row][column] = '.'
            return (new_row, column), killed_targets

    elif command == "shoot":
        matrix[new_row][column] = 'x'
        killed_targets += 1
    return (row, column), killed_targets


def execute_process(matrix, starting_position, side, steps, command, killed_targets):
    row = starting_position[0]
    column = starting_position[1]
    new_starting_position = starting_position

    if side == "right":
        new_column = column + steps
        if new_column < len(matrix):
            new_starting_position, killed_targets = transform_filed_right_left(row, column, new_column, command, killed_targets)

    elif side == "left":
        new_column = column - steps
        if new_column > -1:
            new_starting_position, killed_targets = transform_filed_right_left(row, column, new_column, command, killed_targets)

    elif side == "up":
        new_row = row - steps
        if new_row > -1:
            new_starting_position, killed_targets = transform_filed_up_down(row, column, new_row, command, killed_targets)

    elif side == "down":
        new_row = row + steps
        if new_row < len(matrix):
            new_starting_position, killed_targets = transform_filed_up_down(row, column, new_row, command, killed_targets)

    return matrix, new_starting_position, killed_targets

# Variables
matrix_size = int(input())
matrix = create_matrix(matrix_size)
starting_position = find_starting_position(matrix)
commands_count = int(input())

killed_targets = 0
all_targets_killed = False
for counter in range(commands_count):
    raw_data = input().split()
    command = raw_data[0]
    side = raw_data[1]
    steps = int(raw_data[2])
    check_targets = any([True if 't' in row else False for row in matrix])
    if check_targets:
        matrix, starting_position, killed_targets = execute_process(matrix, starting_position, side, steps, command, killed_targets)
    else:
        all_targets_killed = True
        break

all_targets_killed = any([True if 't' in row else False for row in matrix])
if not all_targets_killed:
    print(f"Mission accomplished! All {killed_targets} targets destroyed.")
else:
    print(f"Mission failed! {sum([row.count('t') for row in matrix if 't' in row])} targets left.")
[print(' '.join(row)) for row in matrix]