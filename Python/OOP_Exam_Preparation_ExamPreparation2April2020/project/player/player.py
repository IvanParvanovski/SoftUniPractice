from abc import abstractmethod, ABC

from project.card.card_repository import CardRepository


class Player(ABC):
    @abstractmethod
    def __init__(self,
                 username: str,
                 health: int):

        self.username = username
        self.health = health
        self.card_repository = CardRepository()

    @staticmethod
    def __is_username_valid(value):
        return True if value else False

    @staticmethod
    def __are_points_valid(value):
        return True if value >= 0 else False

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not Player.__is_username_valid(value):
            raise ValueError("Player's username cannot be an empty string.")
        self._username = value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if not Player.__are_points_valid(value):
            raise ValueError("Player's health bonus cannot be less than zero.")

        self._health = value

    @property
    def is_dead(self):
        return self._health <= 0

    def take_damage(self, damage_points: int):
        if not Player.__are_points_valid(damage_points):
            raise ValueError("Damage points cannot be less than zero.")

        self.health -= damage_points
