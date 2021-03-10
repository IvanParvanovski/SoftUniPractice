# from ex3_players_and_monsters.project.dark_knight import DarkKnight
from project.dark_knight import DarkKnight


class BladeKnight(DarkKnight):
    def __init__(self, username: str, level: int):
        super().__init__(username, level)
