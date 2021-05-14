from collections import deque
from types import SimpleNamespace


class Player:
    def __init__(self,
                 row,
                 col):

        self.row = row
        self.col = col


class Game:
    def __init__(self,
                 playground,
                 player: Player):

        self.playground = playground
        self.player = player
        self.lost = False

    def __enter__(self):
        """
        Checks if the player has lost the game
        :return: self -> the current object
        """


        if self.has_fallen():
            self.lost = True

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Changes the symbol behind the player
        Changes the position of the player (row - 1)

        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return: None
        """

        if self.player.row == len(self.playground) - 1:
            previous_symbol = '0'
        else:
            previous_symbol = '-'

        self.playground[self.player.row][self.player.col] = previous_symbol
        self.player.row -= 1
        self.playground[self.player.row][self.player.col] = 'S'

    def has_fallen(self):
        """
        Checks if the player has stepped on 0 or something else

        :return: bool
        """

        current_row = self.playground[self.player.row - 1]

        if not current_row[self.player.col] == '-':
            return True

        return False


def rotate_position(current_row,
                    steps_to_rotate_,):
    """
    Pops and inserts a value n-times

    :param current_row:
    :param steps_to_rotate_:
    :return: Deque(current_row)
    """
    current_row_deque = deque(current_row)

    for _ in range(steps_to_rotate_):
        current_row_deque.insert(0, current_row_deque.pop())

    return current_row_deque


rows_count, columns_count = map(int, input().split())
playground = [list(input()) for _ in range(rows_count)]

player = Player(row=rows_count - 1,
                col=playground[-1].index('S'))

result_data = SimpleNamespace(win_or_lose='win',
                              total_jumps=0)

turns_count = int(input())

for _ in range(turns_count):
    row_to_rotate_index, steps_to_rotate = map(int, input().split())
    row_to_rotate_index -= 1

    row_to_rotate = playground[row_to_rotate_index]
    playground[row_to_rotate_index] = rotate_position(row_to_rotate,
                                                      steps_to_rotate)

    result_data.total_jumps += 1

    with Game(playground, player) as g:
        if g.lost:
            result_data.win_or_lose = 'lose'
            break

try:
    playground[0].index('S')
except ValueError:
    result_data.win_or_lose = 'lose'

print(result_data.win_or_lose.capitalize())
print(f'Total jumps: {result_data.total_jumps}')

for row in playground:
    print(''.join(row))
