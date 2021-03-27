# NOT WORKING !!!


from typing import NamedTuple


class Bord(NamedTuple):
    first_row: list
    second_row: list
    third_row: list


class TikTacToe:
    def __init__(self, board):
        self.board = board

    def has_winner(self):
        return any((self.is_winner(1), self.is_winner(2)))

    def is_winner(self, player_number):
        player_row, player_col = self._player_index(player_number)
        return any((
            self._is_winner_row(player_col, player_number),
            self._is_winner_col(player_row, player_number),
            self._is_winner_cross(player_number),
        ))

    # def _player_index(self, player_number):
    #     for row in self.board:
    #         for col in row:
    #             if self.board[row][col] == player_number:
    #                 return row, col
    #     return None

    # def _is_winner_row(self, player_col, player_num):
    #     previous_col = 0
    #     for row in self.board:
    #         if self.board[][previous_col] !=
    #     return True

    def _is_winner_col(self, player_row, player_num):
        board_row = self.board[player_row]
        for col in board_row:
            if col != player_num:
                return False
        return True

    def _is_winner_cross(self, player_num):
        previous_col = 0
        for row in self.board:
            if player_num != row[previous_col]:
                return False
            previous_col += 1
        return True


def read_fields(fields_count: int) -> list:
    board_list = list()

    for _ in range(fields_count):
        user_input = tuple(int(x) for x in input().split())
        assert len(user_input) == fields_count, ('fields_count != user_input_fields_count, ' 
                                                 'Less Numbers were given!')
        board_list.append(user_input)

    return board_list


my_board = Bord(*read_fields(3))
print(my_board)
print(TikTacToe(my_board).has_winner())
