# from ex3_players_and_monsters.project.knight import Knight
from project.knight import Knight


class DarkKnight(Knight):
    def __init__(self, username: str, level: int):
        super().__init__(username, level)

