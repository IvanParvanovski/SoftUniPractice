from project.player.player import Player


class Beginner(Player):
    def __init__(self, username):
        Player.__init__(self, username, 50)
