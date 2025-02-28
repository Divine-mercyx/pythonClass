class SevenSegment:

    def __init__(self):
        self.__board = [
            [" ", " ", " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "]
        ]


    def draw_one(self):
        for row in range(len(self.__board)):
            if row == 2:
                continue
            self.__board[row][3] = "#"
        return self.__board

    def draw_two(self):
        for col in range(len(self.__board[0])):
            self.__board[0][col] = "#"

        for col in range(len(self.__board[0])):
            self.__board[2][col] = "#"

        for col in range(len(self.__board[0])):
            self.__board[4][col] = "#"

        self.__board[1][3] = "#"
        self.__board[3][0] = "#"

        return self.__board

    def draw_three(self):
        for col in range(len(self.__board[0])):
            self.__board[0][col] = "#"

        for col in range(len(self.__board[0])):
            self.__board[2][col] = "#"

        for col in range(len(self.__board[0])):
            self.__board[4][col] = "#"

        self.__board[1][3] = "#"
        self.__board[3][3] = "#"

        return self.__board

    def draw_four(self):
        self.__board[0][0] = "#"
        self.__board[0][3] = "#"
        self.__board[1][0] = "#"
        self.__board[1][3] = "#"
        for col in range(len(self.__board[0])):
            self.__board[2][col] = "#"
        self.__board[3][3] = "#"
        self.__board[4][3] = "#"
        return self.__board

    def draw_five(self):
        for col in range(len(self.__board[0])):
            self.__board[0][col] = "#"

        for col in range(len(self.__board[0])):
            self.__board[2][col] = "#"

        for col in range(len(self.__board[0])):
            self.__board[4][col] = "#"

        self.__board[1][0] = "#"
        self.__board[3][3] = "#"

        return self.__board

    def draw_six(self):
        for col in range(len(self.__board[0])):
            self.__board[0][col] = "#"

        for col in range(len(self.__board[0])):
            self.__board[2][col] = "#"

        for col in range(len(self.__board[0])):
            self.__board[4][col] = "#"

        self.__board[1][0] = "#"
        self.__board[3][3] = "#"
        self.__board[3][0] = "#"
        return self.__board

    def draw_seven(self):
        for col in range(len(self.__board[0])):
            self.__board[0][col] = "#"
        for row in range(1, 5):
            self.__board[row][3] = "#"
        return self.__board

    def draw_eight(self):
        for col in range(len(self.__board[0])):
            self.__board[0][col] = "#"

        for col in range(len(self.__board[0])):
            self.__board[2][col] = "#"

        for col in range(len(self.__board[0])):
            self.__board[4][col] = "#"

        self.__board[1][0] = "#"
        self.__board[1][3] = "#"
        self.__board[3][3] = "#"
        self.__board[3][0] = "#"
        return self.__board

    def draw_nine(self):
        for col in range(len(self.__board[0])):
            self.__board[0][col] = "#"

        for col in range(len(self.__board[0])):
            self.__board[2][col] = "#"

        for col in range(len(self.__board[0])):
            self.__board[4][col] = "#"

        self.__board[1][0] = "#"
        self.__board[1][3] = "#"
        self.__board[3][3] = "#"
        return self.__board