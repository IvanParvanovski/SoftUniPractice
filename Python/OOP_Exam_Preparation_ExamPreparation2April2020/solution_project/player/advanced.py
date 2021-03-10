from project.player.player import Player


class Advanced(Player):
    def __init__(self, username):
        Player.__init__(self, username, 250)
