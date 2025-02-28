class Board:
    def __init__(self):
        self.__board = [" "] * 9
        self.__string_board = """

          {0} | {1} | {2}
         -----------
          {3} | {4} | {5}
         -----------
          {6} | {7} | {8}

        """


    def get_board(self):
        return self.__board

    def check_win(self, player):
        win_conditions = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]
        for a, b, c in win_conditions:
            if {self.__board[a], self.__board[b], self.__board[c]} == {player}:
                return True

    def check_if_tied(self):
        if " " in self.__board: return False
        return True



    def play_move(self, token: str, move: int):
        if move < 1 or move > 9: raise ValueError("Invalid move")
        if self.__board[move - 1] != " ": raise ValueError("Invalid move, position already filled")
        self.__board[move - 1] = token

    def display_board(self):
        return self.__string_board.format(*self.get_board())