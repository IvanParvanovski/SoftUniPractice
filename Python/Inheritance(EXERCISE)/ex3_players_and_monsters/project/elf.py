# from ex3_players_and_monsters.project.hero import Hero
from project.hero import Hero


class Elf(Hero):
    def __init__(self, username: str, level: int):
        super().__init__(username, level)
