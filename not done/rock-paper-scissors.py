import random
#Chris' section

def home_screen(): #this function is the starting point, it is only called once and asks if you would like instructions for the game or if you would simply like to start playing.
    print()
    print()
    print("this script is a bit simplistic; please enter your choices in full, for example: 'Start' instead of 's' or '2'.")
    print()
    print()
    instructions_or_start = input("Instructions or start? ")
    if instructions_or_start.lower() == "instructions":
        print()
        print()
        print("This is a script that plays a game of 'Rock Paper Scissors'. The objective of the game is to pick an option that 'beats' the option your opponent chose.")
        print("Possible options include: 'Rock', 'Paper', and 'Scissors', as the name implies. with the rules going as follows: Paper covers Rock, Rock smashes Scissors, and Scissors cut Paper.")
        print("If both players choose the same option the game ends in a draw, which in this script counts as a loss for both players.")
        home_screen()
    elif instructions_or_start.lower() == "start":
        player_number_calculator()
    else:
        home_screen()

def player_number_calculator(): #this function is very simple, only being called once and only being used to determine how many players will be playing between one or two.
    print()
    print()
    player_number = input("1 or 2 players? ")
    if player_number == '1':
        battle()
    elif player_number == '2':
        print("two players")
    else:
        print()
        print()
        print("apologies, you have input something that doesnt compute.")
        player_number_calculator()

def quit_or_continue(): #this will be called at the end of every game.
    print()
    print()
    continueyn = input("would you like to continue? (y/n) ")
    if continueyn.lower() == "y":
        battle()
    elif continueyn.lower() == "n":
        print()
        print()
        print("goodbye")
    else:
        quit_or_continue()
        
#NEW SCRIPT (semi comlete) down below
#Alvin's section
def battle():
    print()
    print()
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print()
    print()
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    print()
    print()
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie... NERD!")
    elif user_action == "rock":
        if computer_action  == "scissors":
            print("rock beats scissors, you win.")
        else:
            print("paper covers rock, you lose... LOSER")
    elif user_action == "paper":
        if computer_action == "rock":
            print("paper covers rock! you win.")
        else:
            print("scissors cuts paper, you lose... LOSER NERD")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("scissors cuts paper, you win.")
        else:
            print("rock smashes scissors, you lose... IMBECIL")
    else:
        print("you have to pick between rock, paper and scissors, not something random... NERD")

    quit_or_continue()


home_screen()
