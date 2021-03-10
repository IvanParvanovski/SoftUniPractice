class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players_list = list()

    def is_player_already_in_the_guild(self, player):
        return player in self.players_list

    def does_player_have_guild(self, player):
        return player.guild != "Unaffiliated"

    def assign_player(self, player):
        if self.is_player_already_in_the_guild(player):
            return f"Player {player.name} is already in the guild."

        if self.does_player_have_guild(player):
            return f"Player {player.name} is in another guild."

        player.guild = self.name
        self.players_list.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        player_to_remove = [player for player in self.players_list if player.name == player_name]

        if not player_to_remove:
            return f"Player {player_name} is not in the guild."

        player = player_to_remove[0]
        self.players_list.remove(player)
        return f"Player {player.name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"

        for player in self.players_list:
            result += f"{player.player_info()}"

        return result
