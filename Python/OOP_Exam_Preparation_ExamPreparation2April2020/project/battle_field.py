from project.player.player import Player


class BattleField:
    @staticmethod
    def __does_fight_contain_dead_player(first_player: Player,
                                         second_player: Player):

        return first_player.is_dead or second_player.is_dead

    @staticmethod
    def __is_player_beginner(player: Player):
        if not type(player).__name__ == 'Beginner':
            return

        player.health += 40
        for card in player.card_repository.cards:
            card.damage_points += 30

    @staticmethod
    def __get_bonus_health(player: Player):
        player.health += sum(card.health_points for card in player.card_repository.cards)

    @staticmethod
    def fight(attacker: Player, enemy: Player):
        if BattleField.__does_fight_contain_dead_player(attacker, enemy):
            raise ValueError('Player is dead!')

        BattleField.__is_player_beginner(attacker)
        BattleField.__is_player_beginner(enemy)

        BattleField.__get_bonus_health(attacker)
        BattleField.__get_bonus_health(enemy)

        for c in attacker.card_repository.cards:
            if enemy.is_dead or attacker.is_dead:
                return

            enemy.take_damage(c.damage_points)

        for c in enemy.card_repository.cards:
            if enemy.is_dead or attacker.is_dead:
                return

            attacker.take_damage(c.damage_points)
