import random
from rock_paper_scissors import player_number_calculator, choose_your_actions, quit_or_continue

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
        print("instuctions to be added")
    elif instructions_or_start == "start":
        print("start")
    else:
        home_screen()
