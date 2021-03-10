import unittest

from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.pr = PlayerRepository()
        self.player = Beginner('IVP')
        self.pr.add(self.player)

    def test_playerRepositoryAdd_whenPlayerExist_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            self.pr.add(self.player)

        self.assertIsNotNone(context.exception)
        self.assertEqual(1, self.pr.count)

    def test_playerRepositoryRemove_whenPlayerStringIsInvalid_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            self.pr.remove('')

        self.assertIsNotNone(context.exception)

    def test_playerRepositoryRemove_whenPlayerNameIsValid_shouldRemovePlayer(self):
        expected_count = 0
        expected_list = list()

        self.pr.remove('IVP')
        actual_count = self.pr.count
        actual_list = self.pr.players

        self.assertListEqual(expected_list, actual_list)
        self.assertEqual(expected_count, actual_count)

    def test_playerRepositoryFind_whenPlayerExists_shouldReturnPlayer(self):
        actual_player = self.pr.find('IVP')

        self.assertEqual(self.pr.players[0], actual_player)


if __name__ == '__main__':
    unittest.main()
