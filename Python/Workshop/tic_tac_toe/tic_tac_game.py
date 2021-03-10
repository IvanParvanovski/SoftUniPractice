from tic_tac_toe.checks import check_if_user_position_is_valid, check_if_position_is_already_taken, check_game_over_draw, check_game_over_winner
from tic_tac_toe.transform_data import get_position
from tic_tac_toe.printing import print_welcome, print_board, print_game_over_winner, print_game_over_draw
from tic_tac_toe.setup import setup


def place_mark(board: list, player, board_size) -> None:
    while True:
        (row, column) = get_position(player, board_size)

        if check_if_user_position_is_valid(row, column, board_size):
            continue

        elif check_if_position_is_already_taken(board, row, column):
            continue

        else:
            board[row][column] = player.mark
            break


def game_loop(board, players, board_size):
    current_player, next_player = players
    while True:
        place_mark(board, current_player, board_size)
        if check_game_over_winner(board, current_player, board_size):
            print_game_over_winner(board, current_player)
            break
        elif not check_game_over_draw(board):
            print_game_over_draw(board)
            break

        print_board(board)
        current_player, next_player = next_player, current_player


def start_game(board_size):
    (board, *players) = setup(board_size)
    print_welcome(players[0], board_size)
    game_loop(board, players, board_size)
