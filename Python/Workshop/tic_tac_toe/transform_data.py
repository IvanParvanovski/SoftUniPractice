def get_each_column_values(board: list, board_size) -> list:
    columns_values = list()
    for column in range(board_size):
        new_values = list()
        for row in range(board_size):
            new_values.append(board[row][column])
        columns_values.append(new_values)
    return columns_values


def get_main_and_secondary_diagonal_values(board: list, board_size) -> list:
    result = [
        [board[i][i] for i in range(board_size)],
        [board[i][board_size - i - 1] for i in range(board_size)]
    ]

    return result


def get_position(player, board_size) -> tuple:
    while True:
        position = input(f"{player.name} chooses a free position [1-9]: ")
        if position.isdigit():
            break
        print("Please enter a number! ")
    position = int(position)
    row = (position - 1) // board_size
    column = (position - 1) % board_size
    return row, column
