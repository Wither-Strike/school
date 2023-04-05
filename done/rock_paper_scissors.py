import random
# Chris' section

def home_screen():
    print()
    print()
    print("This script is a bit simplistic; please enter your choices in full, for example: 'Start' instead of 's' or '2'.")
    print()
    print()
    instructions_or_start = input("Instructions or start? ").lower()
    if instructions_or_start == "instructions":
        print()
        print()
        print("This is a script that plays a game of 'Rock Paper Scissors'. The objective of the game is to pick an option that 'beats' the option your opponent chose.")
        print("Possible options include: 'Rock', 'Paper', and 'Scissors', as the name implies. with the rules going as follows: Paper covers Rock, Rock smashes Scissors, and Scissors cut Paper.")
        print("If both players choose the same option the game ends in a draw, which in this script counts as a loss for both players.")
        home_screen()
    elif instructions_or_start == "start":
        player_number_calculator()
    else:
        home_screen()

# Partially Chris', partially Alvins

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
        battle(user1_choice, user2_choice)
    else:
        user1_choice = input(f"Enter a choice: ({possible_actions})").lower()
        user2_choice = input(f"Enter a choice: ({possible_actions})").lower()
        battle(user1_choice, user2_choice)


def quit_or_continue():
    print()
    print()
    print(f"player 1s score is {p1score} against player 2s {p2score}")
    print()
    print()
    continueyn = input("would you like to continue? (y/n) ").lower()
    if continueyn == "y":
        player_number_calculator()
    elif continueyn == "n":
        write_file()
        print()
        print()
        print("goodbye")
    else:
        quit_or_continue()
        
# NEW SCRIPT (semi comlete) down below
# Alvins section
def battle(user_action1, user_action2):
    global  p1score, p2score
    print()
    print()
    print(f"\nuser 1 chose {user_action1}, user 2 chose {user_action2}.\n")
    print()
    print()
    if user_action1 == user_action2:
        print(f"Both players selected {user_action1}. It's a tie... NERD!")
        p1score += 1
        p2score += 1
    elif user_action1 == "rock":
        if user_action2  == "scissors":
            print("rock beats scissors, you win.")
            p1score += 1
        else:
            print("paper covers rock, you lose... LOSER")
            p2score += 1
    elif user_action1 == "paper":
        if user_action2 == "rock":
            print("paper covers rock! you win.")
            p1score += 1
        else:
            print("scissors cuts paper, you lose... LOSER NERD")
            p2score += 1
    elif user_action1 == "scissors":
        if user_action2 == "paper":
            print("scissors cuts paper, you win.")
            p1score += 1
        else:
            print("rock smashes scissors, you lose... IMBECIL")
            p2score += 1
    else:
        print("you have to pick between rock, paper and scissors, not something random... NERD")

    quit_or_continue()

p1score = 0
p2score = 0
ratio = None
playername = input("input name:")

try:
    open(f"{playername}.txt", "r")
except:
    with open(f"{playername}.txt", "x") as file:
        file.write('0.0')

def write_file():
    with open(f"{playername}.txt", "r+") as file:
        ratio = p1score/(p1score+p2score)
        #print(type(file.read().rstrip()))
        fromfile = float(file.read().rstrip())
        #print(type(fromfile))
        if fromfile < ratio:
            ratio = ratio.__str__()
            with open(f"{playername}.txt", "w") as f:
                f.write(ratio)

home_screen()
