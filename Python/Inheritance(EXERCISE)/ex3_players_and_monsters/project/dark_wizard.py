# from ex3_players_and_monsters.project.wizard import Wizard
from project.wizard import Wizard


class DarkWizard(Wizard):
    def __init__(self, username: str, level: int):
        super().__init__(username, level)
