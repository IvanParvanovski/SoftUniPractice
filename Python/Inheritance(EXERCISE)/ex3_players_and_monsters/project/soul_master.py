# from ex3_players_and_monsters.project.dark_wizard import DarkWizard
from project.dark_wizard import DarkWizard


class SoulMaster(DarkWizard):
    def __init__(self, username: str, level: int):
        super().__init__(username, level)
