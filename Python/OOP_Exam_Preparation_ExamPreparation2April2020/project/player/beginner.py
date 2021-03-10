from project.player.player import Player


class Beginner(Player):
    def __init__(self,
                 username: str):

        health = 50
        super().__init__(username, health)
