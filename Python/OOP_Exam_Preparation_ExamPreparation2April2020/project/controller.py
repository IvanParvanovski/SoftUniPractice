from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def __find_player(self, username):
        return self.player_repository.find(username)

    def __find_card(self, card):
        return self.card_repository.find(card)

    def add_player(self, type: str, username: str):
        players_types = {'Beginner': Beginner,
                         'Advanced': Advanced}

        player = players_types[type](username)
        self.player_repository.add(player)

        return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type: str, name: str):
        cards_types = {'Magic': MagicCard,
                       'Trap': TrapCard}

        card = cards_types[type](name)
        self.card_repository.add(card)

        return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username: str, card_name: str):
        player = Controller.__find_player(self, username)
        card = Controller.__find_card(self, card_name)

        player.card_repository.add(card)

        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name: str, enemy_name: str):
        attacker = Controller.__find_player(self, attack_name)
        enemy = Controller.__find_player(self, enemy_name)

        BattleField().fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        result = ''

        for player in self.player_repository.players:
            result += f'Username: {player.username} - ' \
                      f'Health: {player.health} - ' \
                      f'Cards {player.card_repository.count}\n'

            for card in player.card_repository.cards:
                result += f'### Card: {card.name} - Damage: {card.damage_points}\n'

        return result
