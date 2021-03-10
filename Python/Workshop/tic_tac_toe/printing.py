from tic_tac_toe.setup import create_welcome_board


def print_welcome(player, board_size) -> None:
    print("This is the numeration of the board")
    create_welcome_board(board_size)
    print(f"{player.name} starts first!")


def print_board(board: list) -> list:
    return [print(f"| {' | '.join(token)} |") for token in board]


def print_game_over_winner(board, player):
    print_board(board)
    print(f"{player.name} won!")


def print_game_over_draw(board):
    print_board(board)
    print(f"Draw!")
