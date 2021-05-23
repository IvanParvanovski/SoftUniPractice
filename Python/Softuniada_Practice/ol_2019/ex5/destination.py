from copy import copy


class Destination:
    def __init__(self,
                 hero_col,
                 hero_row,
                 wanted_col,
                 wanted_row,
                 field_cols,
                 field_rows,
                 previous_direction):

        self.hero_col = hero_col
        self.hero_row = hero_row

        self.wanted_col = wanted_col
        self.wanted_row = wanted_row

        self.field_cols = field_cols
        self.field_rows = field_rows

        self.previous_direction = previous_direction

        self.directions = {
            'left': False,
            'right': False,
            'up': False,
            'down': False,
        }

    def set_possible_movements(self):
        if -1 < self.hero_row - 1:
            self.directions['up'] = True

        if self.hero_row + 1 < self.field_rows:
            self.directions['down'] = True

        if -1 < self.hero_col - 1:
            self.directions['left'] = True

        if self.hero_col + 1 < self.field_cols:
            self.directions['right'] = True

    def set_impossible_movements(self, directions):
        directions_copy = copy(directions)
        directions_opposite = {
            'left': 'right',
            'right': 'left',
            'up': 'down',
            'down': 'up',
        }

        if self.hero_col < self.wanted_col:
            directions_copy['left'] = False
        elif self.hero_col > self.wanted_col:
            directions_copy['right'] = False

        if self.hero_row < self.wanted_row:
            directions_copy['up'] = False
        elif self.hero_row > self.wanted_row:
            directions_copy['down'] = False

        directions_copy[directions_opposite[self.previous_direction]] = False
        directions_copy[self.previous_direction] = False

        return directions_copy

    def set_new_direction(self):
        for track in self.directions:
            if self.directions[track]:
                return track

    def change_direction(self):
        self.set_possible_movements()
        self.directions = self.set_impossible_movements(self.directions)
        return self.set_new_direction()
