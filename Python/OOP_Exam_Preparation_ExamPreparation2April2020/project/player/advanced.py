from project.player.player import Player


class Advanced(Player):
    def __init__(self,
                 username: str):

        health = 250
        super().__init__(username, health)
