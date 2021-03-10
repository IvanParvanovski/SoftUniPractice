from project.player.player import Player



class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        try:
            player = [p for p in self.players if p.username == player.username][0]
            raise ValueError(f"Player {player.username} already exists!")
        except IndexError:
            self.players.append(player)
            self.count += 1

    # Be careful - here the param player is a string not the
    # player object
    def remove(self, player: str):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        p = [p for p in self.players if p.username == player][0]
        self.players.remove(p)
        self.count -= 1

    def find(self, username: str):
        p = [p for p in self.players if p.username == username][0]
        return p


# from project.player.beginner import Beginner
#
# p = Beginner("test")
#
# pr = PlayerRepository()
# pr.add(p)
# print(pr.count)
# print(pr.find("test"))
