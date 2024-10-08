import random

def home_screen():
    print("\n\nThis script is a bit simplistic; please enter your choices in full, for example: 'Start' instead of 's' or '2'.\n\n")
    instructions_or_start = input("Instructions or start?\n").lower()
    if instructions_or_start == "instructions":
        print("\n\nTic-tac-toe is a pencil and paper game played on a 3X3 grid, the two players are represented by different symbols\n\
(commonly X's and O's, hence the alternative name of 'noughts and crosses'). The game is played by placing your symbol into an empty space on the grid.\n\
The goal of the game is to place three of your symbols in a row before your opponent, vertical lines horizontal lines and diagonal lines are all accepted\n\
for this win condition. for this version of the game to tell where the player wishes to place their symbol the script looks for input in the format of letternumber\n\
(for example: a1, b2, b3)")
        home_screen()
    elif instructions_or_start == "start":
        player_number_calculator()
    else:
        home_screen()

def player_number_calculator():
    player_number = input("\n\n1 or 2 players?\n")
    if player_number == "1":
        choose_your_actions(3)
    if player_number == "2":
        choose_your_actions(1)
    else:
        print("\n\nYou have input something that does not compute")
        player_number_calculator()

possible_actions = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]

def choose_your_actions(active_player_number):
    if active_player_number == 1:
        X_choice = input(f"\n\nEnter a choice:({possible_actions})\n").lower()
        if X_choice not in possible_actions:
            print("\n\nthat move is not availible, try again\n\n")
            choose_your_actions(1)
        player_choice_to_board(X_choice, 1)
    if active_player_number == 2:
        O_choice = input(f"\n\nEnter a choice:({possible_actions})\n").lower()
        if O_choice not in possible_actions:
            print("\n\nthat move is not availible, try again\n\n")
            choose_your_actions(2)
            choose_your_actions(1)
        player_choice_to_board(O_choice, 2)
    if active_player_number == 3:
        X_choice = input(f"\n\nEnter a choice:({possible_actions})\n").lower()
        if X_choice not in possible_actions:
            print("\n\nthat move is not availible, try again\n\n")
            choose_your_actions(3)
        else:
            player_choice_to_board(X_choice, 3)


move_counter = 0

a1 = " "
a2 = " "
a3 = " "
b1 = " "
b2 = " "
b3 = " "
c1 = " "
c2 = " "
c3 = " "
board = f"  1  2  3\nA {a1} | {a2} | {a3} \n——————————————————————\nB {b1} | {b2} | {b3} \n——————————————————————\nC {c1} | {c2} | {c3}"

def printboard():
    global board
    board = f"  1  2  3\nA {a1} | {a2} | {a3} \n——————————————————————\nB {b1} | {b2} | {b3} \n——————————————————————\nC {c1} | {c2} | {c3}"
    print(board)

def player_choice_to_board(choice, active_player_number):
    global a1, a2, a3, b1, b2, b3, c1, c2, c3, board, move_counter
    move_counter += 1
    if choice == "a1":
        possible_actions.remove("a1")
        if active_player_number == 1:
            a1 = "X"
            printboard()
            winner_question_mark(2)
            winner_question_mark(1)
        elif active_player_number == 2:
            a1 = "O"
            printboard()
        elif active_player_number == 3:
            a1 = "X"
            printboard()
            winner_question_mark(3)

    if choice == "a2":
        possible_actions.remove("a2")
        if active_player_number == 1:
            a2 = "X"
            printboard()
            winner_question_mark(2)
            winner_question_mark(1)
        elif active_player_number == 2:
            a2 = "O"
            printboard()
        elif active_player_number == 3:
            a2 = "X"
            printboard()
            winner_question_mark(3)
            
    if choice == "a3":
        possible_actions.remove("a3")
        if active_player_number == 1:
            a3 = "X"
            printboard()
            winner_question_mark(2)
            winner_question_mark(1)
        elif active_player_number == 2:
            a3 = "O"
            printboard()
        elif active_player_number == 3:
            a3 = "X"
            printboard()
            winner_question_mark(3)
            
    if choice == "b1":
        possible_actions.remove("b1")
        if active_player_number == 1:
            b1 = "X"
            printboard()
            winner_question_mark(2)
            winner_question_mark(1)
        elif active_player_number == 2:
            b1 = "O"
            printboard()
        elif active_player_number == 3:
            b1 = "X"
            printboard()
            winner_question_mark(3)
            
    if choice == "b2":
        possible_actions.remove("b2")
        if active_player_number == 1:
            b2 = "X"
            printboard()
            winner_question_mark(2)
            winner_question_mark(1)
        elif active_player_number == 2:
            b2 = "O"
            printboard()
        elif active_player_number == 3:
            b2 = "X"
            printboard()
            winner_question_mark(3)
            
    if choice == "b3":
        possible_actions.remove("b3")
        if active_player_number == 1:
            b3 = "X"
            printboard()
            winner_question_mark(2)
            winner_question_mark(1)
        elif active_player_number == 2:
            b3 = "O"
            printboard()
        elif active_player_number == 3:
            b3 = "X"
            printboard()
            winner_question_mark(3)
            
    if choice == "c1":
        possible_actions.remove("c1")
        if active_player_number == 1:
            c1 = "X"
            printboard()
            winner_question_mark(2)
            winner_question_mark(1)
        elif active_player_number == 2:
            c1 = "O"
            printboard()
        elif active_player_number == 3:
            c1 = "X"
            printboard()
            winner_question_mark(3)
            
    if choice == "c2":
        possible_actions.remove("c2")
        if active_player_number == 1:
            c2 = "X"
            printboard()
            winner_question_mark(2)
            winner_question_mark(1)
        elif active_player_number == 2:
            c2 = "O"
            printboard()
        elif active_player_number == 3:
            c2 = "X"
            printboard()
            winner_question_mark(3)
            
    if choice == "c3":
        possible_actions.remove("c3")
        if active_player_number == 1:
            c3 = "X"
            printboard()
            winner_question_mark(2)
            winner_question_mark(1)
        elif active_player_number == 2:
            c3 = "O"
            printboard()
        elif active_player_number == 3:
            c3 = "X"
            printboard()
            winner_question_mark(3)
            

def winner_question_mark(active_player_number):
    global p1score, p2score
    if (a1 == a2 and a1 == a3 and a1 == "X") or (b1 == b2 and b1 == b3 and b1 == "X") or (c1 == c2 and c1 == c3 and c1 == "X") or (a1 == b1 and a1 == c1 and a1 == "X") or (a2 == b2 and a2 == c2 and a2 == "X") or (a3 == b3 and a3 == c3 and a3 == "X") or (a1 == b2 and a1 == c3 and a1 == "X") or (a3 == b2 and a3 == c1 and a3 == "X"):
        print("The winner is X!")
        p1score += 1
        quit_or_continue()
    elif (a1 == a2 and a1 == a3 and a1 == "O") or (b1 == b2 and b1 == b3 and b1 == "O") or (c1 == c2 and c1 == c3 and c1 == "O") or (a1 == b1 and a1 == c1 and a1 == "O") or (a2 == b2 and a2 == c2 and a2 == "O") or (a3 == b3 and a3 == c3 and a3 == "O") or (a1 == b2 and a1 == c3 and a1 == "O") or (a3 == b2 and a3 == c1 and a3 == "O"):
        print("The winner is O!")
        p2score += 1
        quit_or_continue()
    elif move_counter == 9:
        print("It's a draw!")
        quit_or_continue()
    else:
        if active_player_number == 1:
            choose_your_actions(1)
        elif active_player_number == 2:
            choose_your_actions(2)
        else:
            player_choice_to_board(random.choice(possible_actions), 2)
            choose_your_actions(3)

def quit_or_continue():
    continueyn = input("\n\nwould you like to continue? (y/n)\n").lower()
    if continueyn == "y":
        global possible_actions, a1, a2, a3, b1, b2, b3, c1, c2, c3, move_counter
        move_counter = 0
        possible_actions = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
        a1 = " "
        a2 = " "
        a3 = " "
        b1 = " "
        b2 = " "
        b3 = " "
        c1 = " "
        c2 = " "
        c3 = " "
        player_number_calculator()
    elif continueyn == "n":
        print("\n\ngoodbye")

    else:
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
