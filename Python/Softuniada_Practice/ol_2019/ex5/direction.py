from abc import abstractmethod, ABC


class Direction(ABC):
    def __init__(self, row, col):
        self.row = row
        self.col = col

    @abstractmethod
    def apply(self):
        pass
