# from ex3_players_and_monsters.project.elf import Elf
from project.elf import Elf


class MuseElf(Elf):
    def __init__(self, username: str, level: int):
        super().__init__(username, level)
