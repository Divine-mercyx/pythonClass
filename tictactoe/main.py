from board import Board
from player import Player


def register_first_player():
    name1 = input("enter our name: ")
    while not name1:
        print("invalid name, try again")
        name1 = input("enter our name: ")
    token1 = input("enter your token: ")
    while token1.strip().lower() not in ["x", "o"]:
        print("invalid token, try again!")
        token1 = input("enter your token: ").strip().lower()
    player = Player(name1, token1)
    return player, token1

def choose_player2_token(first_player_token):
    return "o" if first_player_token == "x" else "x"


def register_player_two(first_player_token):
    name2 = input("enter your name: ")
    token2 = choose_player2_token(first_player_token)
    player2 = Player(name2, token2)
    return player2


players = []
player1, first_token = register_first_player()
players.append(player1)
print(player1)
player2 = register_player_two(first_token)
players.append(player2)
print(player2)
board = Board()
counter = 0

while counter < 9:
    if board.check_win(players[1].get_token()):
         print(f"player {players[1].get_name()} wins!")
         break
    if board.check_if_tied():
         print("game is tied")
         break
    square = input(f"player {players[0].get_name()} choose a square: ")
    if not square.isdigit() or not 1 <= (int(square)) <= 9 or board.get_board()[(int(square) - 1)] != " ":
         print("invalid move")
         continue
    board.play_move(players[0].get_token(), int(square))
    print(board.display_board())
    players = players[::-1]
    counter += 1
