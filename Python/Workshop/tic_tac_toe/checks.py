from tic_tac_toe.transform_data import get_each_column_values
from tic_tac_toe.transform_data import get_main_and_secondary_diagonal_values


def all_single_values_in_sequence(sequence: list, mark_to_check: str) -> bool:
    for value in sequence:
        if value != mark_to_check:
            return False
    return True


def check_if_user_position_is_valid(row, col, board_size):
    check_row_index = True if row > board_size - 1 else False
    check_col_index = True if col > board_size - 1 else False

    if check_row_index and check_col_index:
        print("Invalid mark position!")
        print()
        return True


def check_if_position_is_already_taken(board, row, col):
    if board[row][col] != " ":
        print("Тhe position is already taken!")
        print()
        return True


def check_game_over_draw(board: list) -> bool:
    for tokens in board:
        if " " in tokens:
            return True
    return False


def check_game_over_winner(board: list, player, board_size) -> bool:
    row_checks = [all_single_values_in_sequence(row, player.mark) for row in board]
    columns = get_each_column_values(board, board_size)
    columns_check = [all_single_values_in_sequence(col, player.mark) for col in columns]
    diagonals = get_main_and_secondary_diagonal_values(board, board_size)
    diagonals_checks = [all_single_values_in_sequence(diagonal, player.mark) for diagonal in diagonals]

    all_checks = {*row_checks, *columns_check, *diagonals_checks}
    return any(all_checks)
