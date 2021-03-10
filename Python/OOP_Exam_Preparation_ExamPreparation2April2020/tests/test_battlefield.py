import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(unittest.TestCase):
    def setUp(self) -> None:
        self.bf = BattleField()
        self.attacker = Beginner('Ivan')
        self.enemy = Advanced('Alek')

    def test_battleFieldFight_whenAttackerIsDead_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            self.attacker.health = 0
            self.bf.fight(self.attacker, self.enemy)

        self.assertIsNotNone(context.exception)

    def test_battleFieldFight_whenAttackerIsBeginner_shouldGetBonusHealth(self):
        card_1 = MagicCard('At Mag')
        card_2 = MagicCard('En Mag')
        self.attacker.card_repository.add(card_1)
        self.enemy.card_repository.add(card_2)

        self.bf.fight(self.attacker, self.enemy)

        expected_attacker_health = 165
        expected_attacker_card_damage_points = 35
        actual_attacker_health = self.attacker.health
        actual_attacker_card_damage_points = self.attacker.card_repository.cards[0].damage_points

        expected_enemy_health = 295
        expected_enemy_card_damage_points = 5
        actual_enemy_health = self.enemy.health
        actual_enemy_card_damage_points = self.enemy.card_repository.cards[0].damage_points

        self.assertEqual(expected_attacker_health, actual_attacker_health)
        self.assertEqual(expected_attacker_card_damage_points, actual_attacker_card_damage_points)
        self.assertEqual(expected_enemy_health, actual_enemy_health)
        self.assertEqual(expected_enemy_card_damage_points, actual_enemy_card_damage_points)


if __name__ == '__main__':
    unittest.main()
