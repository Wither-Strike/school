import random

def home_screen():
    print()
    print()
    print("This script is a bit simplistic; please enter your choices in full, for example: 'Start' instead of 's' or '2'.")
    print()
    print()
    instructions_or_start = input("Instructions or start? ").lower()
    print()
    print()
    if instructions_or_start == "instructions":
        print("Tic-tac-toe is a pencil and paper game played on a 3X3 grid, the two players are represented by different symbols\n\
              (commonly X's and O's, hence the alternative name of 'noughts and crosses'). The game is played by placing your symbol into an empty space on the grid.\n\
              The goal of the game is to place three of your symbols in a row before your opponent, vertical lines horizontal lines and diagonal lines are all accepted\n\
              for this win condition. for this version of the game to tell where the player wishes to place their symbol the script looks for input in the format of letternumber\n\
              (for example: a1, b2, b3)")
        home_screen()
    elif instructions_or_start == "start":
        print("start")
    else:
        home_screen()

a1 = " "
a2 = " "
a3 = " "
b1 = " "
b2 = " "
b3 = " "
c1 = " "
c2 = " "
c3 = " "
board = f"   1   2   3\nA {a1} | {a2} | {a3}\n  —————————\nB {b1} | {b2} | {b3}\n  —————————\nC {c1} | {c2} | {c3}"
print(board)

def player_number_calculator():
    print()
    print()
    player_number = input("1 or 2 players? ")
    print()
    print()
    if player_number == "1" or player_number == "2":
        choose_your_actions(player_number)
    else:
        print("You have input something that does not compute")
        player_number_calculator()

possible_actions = ["rock", "paper", "scissors"]

def choose_your_actions(re_player_number):
    if re_player_number == '1' or re_player_number == 1:
        user1_choice = input(f"Enter a choice: ({possible_actions})").lower()
        user2_choice = random.choice(possible_actions)

    else:
        user1_choice = input(f"Enter a choice: ({possible_actions})").lower()
        user2_choice = input(f"Enter a choice: ({possible_actions})").lower()



def quit_or_continue():
    print()
    print()
    continueyn = input("would you like to continue? (y/n) ").lower()
    if continueyn == "y":
        player_number_calculator()
    elif continueyn == "n":
        print()
        print()
        print("goodbye")
    else:
        quit_or_continue()