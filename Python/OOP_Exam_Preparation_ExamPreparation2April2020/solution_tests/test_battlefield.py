import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner




class TestBattleField(unittest.TestCase):
    def test_att_is_ded(self):
        advanced = Advanced("test")
        advanced.health = 0
        advanced_2 = Advanced("test2")
        bf = BattleField()
        with self.assertRaises(ValueError) as ex:
            bf.fight(advanced, advanced_2)
        self.assertEqual(str(ex.exception), "Player is dead!")

    def test_enemy_is_dead(self):
        advanced = Advanced("test")
        advanced_2 = Advanced("test2")
        advanced_2.health = 0
        bf = BattleField()
        with self.assertRaises(ValueError) as ex:
            bf.fight(advanced, advanced_2)
        self.assertEqual(str(ex.exception), "Player is dead!")

    def test_damage_points_and_health_increased_without_cards(self):
        advanced = Advanced("test")
        beginner = Beginner("test2")
        bf = BattleField()
        bf.fight(advanced, beginner)
        self.assertEqual(advanced.health, 250)
        self.assertEqual(beginner.health, 90)


    def test_health_increased_form_cards(self):
        advanced = Advanced("test")
        beginner = Beginner("test2")
        bf = BattleField()
        mc = MagicCard("testmagic")
        advanced.card_repository.add(mc)
        tc = TrapCard("testtrap")
        beginner.card_repository.add(tc)
        bf.fight(advanced, beginner)
        self.assertEqual(advanced.health, 180)
        self.assertEqual(beginner.health, 90)

    def test_dead_player_while_fighting(self):
        advanced = Advanced("test")
        beginner = Beginner("test2")
        bf = BattleField()
        mc = TrapCard("testmagic")
        advanced.card_repository.add(mc)
        mc = TrapCard("testmagic2")
        advanced.card_repository.add(mc)
        mc = TrapCard("testmagic3")
        advanced.card_repository.add(mc)
        tc = MagicCard("testtrap")
        beginner.card_repository.add(tc)
        with self.assertRaises(ValueError) as ex:
            bf.fight(advanced, beginner)
        self.assertEqual(str(ex.exception), "Player's health bonus cannot be less than zero.")

