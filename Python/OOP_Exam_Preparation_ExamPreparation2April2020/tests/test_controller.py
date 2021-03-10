import unittest

from project.controller import Controller


class TestController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()

    def test_controllerAddPlayer_shouldAddNewPlayer(self):
        expected_first_player = 'Beginner'
        expected_second_player = 'Advanced'
        expected_beginner_msg = 'Successfully added player of type Beginner ' \
                                'with username: beginner_test'

        expected_advanced_msg = 'Successfully added player of type Advanced ' \
                                'with username: advanced_test'

        actual_beginner_msg = self.controller.add_player('Beginner', 'beginner_test')
        actual_advanced_msg = self.controller.add_player('Advanced', 'advanced_test')

        actual_first_player = type(self.controller.player_repository.players[0]).__name__
        actual_second_player = type(self.controller.player_repository.players[1]).__name__

        self.assertEqual(expected_first_player, actual_first_player)
        self.assertEqual(expected_second_player, actual_second_player)
        self.assertEqual(expected_beginner_msg, actual_beginner_msg)
        self.assertEqual(expected_advanced_msg, actual_advanced_msg)

    def test_controllerAddCard_shouldAddNewCard(self):
        expected_first_card = 'MagicCard'
        expected_second_card = 'TrapCard'

        expected_magic_card_msg = 'Successfully added card of type MagicCard ' \
                                  'with name: magic_card_test'

        expected_trap_card_msg = 'Successfully added card of type TrapCard ' \
                                 'with name: trap_card_test'

        actual_magic_card_msg = self.controller.add_card('Magic', 'magic_card_test')
        actual_trap_card_msg = self.controller.add_card('Trap', 'trap_card_test')

        actual_first_card = type(self.controller.card_repository.cards[0]).__name__
        actual_second_card = type(self.controller.card_repository.cards[1]).__name__

        self.assertEqual(expected_first_card, actual_first_card)
        self.assertEqual(expected_second_card, actual_second_card)
        self.assertEqual(expected_magic_card_msg, actual_magic_card_msg)
        self.assertEqual(expected_trap_card_msg, actual_trap_card_msg)

    def test_controllerAddPlayerCard_shouldAddPlayerCard(self):
        expected_players_count_before_act = 0
        expected_players_count_after_act = 1

        expected_cards_count_before_act = 0
        expected_cards_count_after_act = 1

        expected_msg = 'Successfully added card: card_test to user: player_test'

        actual_players_count_before_act = self.controller.player_repository.count
        actual_cards_count_before_act = self.controller.card_repository.count

        self.controller.add_player("Beginner", "player_test")
        self.controller.add_card("Magic", "card_test")
        actual_msg = self.controller.add_player_card('player_test', 'card_test')

        actual_players_count_after_act = self.controller.player_repository.count
        actual_cards_count_after_act = self.controller.card_repository.count

        self.assertEqual(expected_players_count_before_act, actual_players_count_before_act)
        self.assertEqual(expected_cards_count_before_act, actual_cards_count_before_act)
        self.assertEqual(actual_msg, expected_msg)
        self.assertEqual(expected_players_count_after_act, actual_players_count_after_act)
        self.assertEqual(expected_cards_count_after_act, actual_cards_count_after_act)

    def test_controllerFight_shouldReturnCorrectMessage(self):
        self.controller.add_player('Beginner', 'beginner')
        self.controller.add_player('Advanced', 'advanced')

        expected_msg = 'Attack user health 250 - Enemy user health 90'
        actual_msg = self.controller.fight("advanced", "beginner")

        self.assertEqual(expected_msg, actual_msg)

    def test_controllerReport_shouldReturnCorrectMessage(self):
        self.controller.add_player('Beginner', 'beginner')
        self.controller.add_player('Advanced', 'advanced')
        self.controller.add_card('Magic', "magic_card_test")
        self.controller.add_player_card('beginner', 'magic_card_test')

        expected_msg = "Username: beginner - " \
                       "Health: 50 - " \
                       "Cards 1\n" \
                       "### Card: magic_card_test - Damage: 5\n" \
                       "Username: advanced - Health: 250 - " \
                       "Cards 0\n"

        actual_msg = self.controller.report()

        self.assertEqual(expected_msg, actual_msg)


if __name__ == '__main__':
    unittest.main()
