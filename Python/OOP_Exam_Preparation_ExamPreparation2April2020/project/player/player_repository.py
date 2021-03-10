from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = list()

    @staticmethod
    def __is_username_valid(value):
        return True if value else False

    def __does_player_exist(self, player: Player):
        return player in self.players

    def add(self, player: Player):
        if PlayerRepository.__does_player_exist(self, player):
            raise ValueError(f"Player {player.username} already exists!")

        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if not PlayerRepository.__is_username_valid(player):
            raise ValueError("Player cannot be an empty string!")

        pl = self.find(player)
        self.players.remove(pl)
        self.count -= 1

    def find(self, username: str):
        return [player for player in self.players if player.username == username][0]
