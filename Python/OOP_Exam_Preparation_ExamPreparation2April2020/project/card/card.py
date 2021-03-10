from abc import abstractmethod, ABC


class Card(ABC):
    @abstractmethod
    def __init__(self,
                 name: str,
                 damage_points: int,
                 health_points: int):

        self.name = name
        self.damage_points = damage_points
        self.health_points = health_points

    @staticmethod
    def __is_username_valid(value):
        return True if value else False

    @staticmethod
    def __are_points_valid(value):
        return True if value >= 0 else False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not Card.__is_username_valid(value):
            raise ValueError("Card's name cannot be an empty string.")

        self._name = value

    @property
    def damage_points(self):
        return self._damage_points

    @damage_points.setter
    def damage_points(self, value):
        if not Card.__are_points_valid(value):
            raise ValueError("Card's damage points cannot be less than zero.")

        self._damage_points = value

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        if not Card.__are_points_valid(value):
            raise ValueError("Card's HP cannot be less than zero.")

        self._health_points = value
