import unittest
from unittest.mock import patch
from blackjack import *


class BlackjackTest(unittest.TestCase):
    def setUp(self):
        self.valid_hand = ['10', '7']
        self.blackjack_hand = ['A', 'K']
        self.bust_hand = ['J', 'K', '2']

    # Happy path testi
    def test_blackjack_hand_vals(self):
        self.assertEqual(calculate_hand(self.valid_hand), 17)
        self.assertEqual(calculate_hand(self.blackjack_hand), 21)
        self.assertEqual(calculate_hand(self.bust_hand), 22)

    def test_player_win(self):
        test_cases = [
            (['6', '7'], ['3', '2']),
            (['6', '7'], ['10', 'K', '10']),
        ]
        for player_hand, dealer_hand in test_cases:
            with self.subTest(player_hand=player_hand, dealer_hand=dealer_hand):
                self.assertEqual(determine_winner(player_hand, dealer_hand), "player")

    def test_dealer_win(self):
        test_cases = [
            (['3', '2'], ['6', '7']),
            (['10', 'K', '10'], ['6', '7']),
        ]
        for player_hand, dealer_hand in test_cases:
            with self.subTest(player_hand=player_hand, dealer_hand=dealer_hand):
                self.assertEqual(determine_winner(player_hand, dealer_hand), "dealer")
    def test_tie(self):
        self.assertEqual(determine_winner(['10', '7'], ['9', '8']), "tie")

    # Validation test
    def test_invalid_card(self):
        with self.assertRaises(KeyError):
            calculate_hand(['10', 'X'])

    def test_invalid_input(self):
        for hand in [None, 2.15]:
            with self.subTest(hand=hand):
                with self.assertRaises(TypeError):
                    calculate_hand(hand)

        with self.assertRaises(ValueError):
            calculate_hand([])

        with self.assertRaises(KeyError):
            calculate_hand([2, 5])

    def test_empty_hand_in_determine_winner(self):
        with self.assertRaises(ValueError):
            determine_winner([], ['6', '7'])

    # Edge case test
    def test_both_bust(self):
        self.assertEqual(determine_winner(self.bust_hand, ['10', '9', '5']), "dealer")

    def test_equal_bust_values(self):
        self.assertEqual(determine_winner(self.bust_hand, self.bust_hand), "dealer")


    # Mock test
    def test_blackjack_player_busts(self):
        with patch('random.choice', side_effect=['10', 'K', '7', '8', '5']):
            with patch('builtins.input', side_effect=['h']):
                with patch('builtins.print') as mock_print:
                    blackjack()
                    mock_print.assert_any_call("You busted! Dealer wins.")

    def test_invalid_move(self): # Preveri edge case inputa
        with patch('random.choice', side_effect=['10', '7', '9', '8', '6', '5']):
            with patch('builtins.input', side_effect=['x', 's']):
                with patch('builtins.print') as mock_print:
                    blackjack()
                    mock_print.assert_any_call("Invalid input!")

suite = unittest.TestLoader().loadTestsFromTestCase(BlackjackTest)
unittest.TextTestRunner().run(suite)