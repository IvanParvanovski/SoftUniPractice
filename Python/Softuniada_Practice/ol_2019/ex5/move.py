from ol_2019.ex5.direction import Direction


class Move:
    def __init__(self, direction: Direction, stamina):
        self.direction = direction
        self.stamina = stamina

    def __enter__(self):
        return self.direction.apply()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stamina -= 1
