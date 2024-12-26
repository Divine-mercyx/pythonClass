#divine's python tic tac toe

def display_board():
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |\n"
    + "-------------" + "\n"
    + "| " + board[3] + " | " + board[4] + " | " + board[5] + " |\n"
    + "-------------" + "\n"
    + "| " + board[6] + " | " + board[7] + " | " + board[8] + " |")


def player_moves():
    count = 1
    while count <= 9:
        if count % 2 == 0:
            add_player_token("X")

            if check_if_won("X"):
                print("player x won")
                break

            if check_if_full():
                print("its a draw")
                break

        else:
            add_player_token("O")

            if check_if_won("O"):
                print("player O won")
                break

            if check_if_full():
                print("its a draw")
                break
        count += 1


def add_player_token(token):
    print("player " + token)
    move = int(input("enter between 1 - 9: "))
    if board[move - 1] != " ":
        print("space already filled, try again.")
        add_player_token(token)
    board[move - 1] = token
    display_board()


def check_if_won(token):
    if board[0] == token and board[1] == token and board[2] == token\
            or board[3] == token and board[4] == token and board[5] == token\
            or board[6] == token and board[7] == token and board[8] == token\
            or board[0] == token and board[4] == token and board[8] == token\
            or board[2] == token and board[4] == token and board[6] == token\
            or board[0] == token and board[3] == token and board[6] == token\
            or board[1] == token and board[4] == token and board[7] == token\
            or board[2] == token and board[5] == token and board[8] == token:
        return True


def check_if_full():
    counter = 0
    for count in range(len(board)):
        if board[count - 1] != " ":
            counter += 1
    if counter == 9:
        return True

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

display_board()
player_moves()