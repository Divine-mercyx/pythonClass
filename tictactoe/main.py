from wapitiCore.net.jsparser.jsparser3 import token_name

from board import Board
from player import Player


def register_first_player(standby_token, players):
    name1 = input("enter our name: ")
    token1 = input("enter your token: ")
    standby_token = token1
    player1 = Player(name1, token1)
    players.append(player1)

def choose_player2_token(standby_token):
    if standby_token == "x": return "o"
    return "x"

def register_player_two(standby_token, players):
    name2 = input("enter your name: ")
    token2 = choose_player2_token(standby_token)
    player2 = Player(name2, token2)
    players.append(player2)


first_player_token = ""
players = []
register_first_player(first_player_token, players)
print(first_player_token)
register_player_two(first_player_token, players)
# first_player = input("enter you name: ")
# first_token = input("enter your token: ")
# first_player_token = first_token
# player1 = Player(first_player, first_player_token)
# players = []
# players.append(player1)
#
# second_player = input("enter you name: ")
# second_player_token = ""
# if first_player_token == "x":
#     second_player_token = "o"
# else:
#     second_player_token = "x"
#
# player2 = Player(second_player, second_player_token)
# players.append(player2)
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
    if not square.isdigit() or not 0 <= (int(square) - 1) <= 8 or board.get_board()[(int(square) - 1)] != " ":
         print("invalid move")
         continue
    board.play_move(players[0].get_token(), int(square))
    print(board.display_board())
    players = players[::-1]
    counter += 1
