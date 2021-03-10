from tic_tac_toe.Player import Player


def setup_board(board_size: int) -> list:
    return [[" "] * board_size for _ in range(board_size)]


def create_welcome_board(board_size: int):
    numbers = list()
    for counter in range(1, board_size * board_size + 1):
        if counter % board_size == 0:
            numbers.append(str(counter))
            print(f"| {' | '.join(numbers)} |")
            numbers = list()
        else:
            numbers.append(str(counter))


def setup_player(mark=None):
    print(" -- Player -- ")
    name = input("Name: ")

    if not mark:
        while True:
            mark = input("Please select your mark: ")
            if mark == 'O' or mark == 'X':
                break
            print("Invalid Mark!")
    else:
        print(f"Your mark is: {mark}")

    return Player(name, mark)


def setup(board_size) -> tuple:
    player_one = setup_player()
    player_two = setup_player('O' if player_one.mark == 'X' else 'X')

    board = setup_board(board_size)
    return board, player_one, player_two