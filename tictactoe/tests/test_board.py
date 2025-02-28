import unittest
from tictactoe.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_board_empty(self):
        self.assertEqual(self.board.get_board(), [" "] * 9)

    def test_play_move_valid(self):
        self.board.play_move("X", 1)
        self.assertEqual(self.board.get_board()[0], "X")

    def test_play_move_invalid_position(self):
        with self.assertRaises(ValueError) as context:
            self.board.play_move("X", 10)
        self.assertEqual(str(context.exception), "Invalid move")

    def test_play_move_already_filled(self):
        self.board.play_move("X", 1)
        with self.assertRaises(ValueError) as context:
            self.board.play_move("O", 1)
        self.assertEqual(str(context.exception), "Invalid move, position already filled")

    def test_check_win_horizontal(self):
        self.board.play_move("X", 1)
        self.board.play_move("X", 2)
        self.board.play_move("X", 3)
        self.assertTrue(self.board.check_win("X"))

    def test_check_win_vertical(self):
        self.board.play_move("O", 1)
        self.board.play_move("O", 4)
        self.board.play_move("O", 7)
        self.assertTrue(self.board.check_win("O"))

    def test_check_win_diagonal(self):
        self.board.play_move("X", 1)
        self.board.play_move("X", 5)
        self.board.play_move("X", 9)
        self.assertTrue(self.board.check_win("X"))

    def test_check_if_tied_false(self):
        self.assertFalse(self.board.check_if_tied())

    def test_check_if_tied_true(self):
        moves = ["X", "O", "X", "X", "O", "X", "O", "X", "O"]
        for i, token in enumerate(moves, 1):
            self.board.play_move(token, i)
        self.assertTrue(self.board.check_if_tied())

    def test_display_board(self):
        self.board.play_move("X", 1)
        board_display = self.board.display_board()
        self.assertIn("X", board_display)
        self.assertIn("|", board_display)
        self.assertIn("-", board_display)


if __name__ == "__main__":
    unittest.main()
