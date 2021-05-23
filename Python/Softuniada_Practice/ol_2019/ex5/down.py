from ol_2019.ex5.direction import Direction


class Down(Direction):
    def __init__(self, row, col):
        super().__init__(row, col)

    def apply(self):
        return self.col, self.row + 1
