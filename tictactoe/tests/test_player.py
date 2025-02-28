import unittest
from tictactoe.player import *

class TestPlayer(unittest.TestCase):
    def test_validate_name_and_token_valid(self):
        validate_name_and_token("Alice", "X")

    def test_validate_name_and_token_empty_name(self):
        with self.assertRaises(ValueError) as context:
            validate_name_and_token("", "X")
        self.assertEqual(str(context.exception), "Name is empty")

    def test_validate_name_and_token_empty_token(self):
        with self.assertRaises(ValueError) as context:
            validate_name_and_token("Alice", "")
        self.assertEqual(str(context.exception), "Token is empty")

    def test_player_creation_valid(self):
        player = Player("Bob", "O")
        self.assertEqual(player.get_name(), "Bob")
        self.assertEqual(player.get_token(), "O")

    def test_player_creation_empty_name(self):
        with self.assertRaises(ValueError) as context:
            Player("", "O")
        self.assertEqual(str(context.exception), "Name is empty")

    def test_player_creation_empty_token(self):
        with self.assertRaises(ValueError) as context:
            Player("Bob", "")
        self.assertEqual(str(context.exception), "Token is empty")

    def test_player_str(self):
        player = Player("Charlie", "X")
        expected_output = "name: Charlie\ntoken: X\n"
        self.assertEqual(str(player), expected_output)


if __name__ == "__main__":
    unittest.main()
