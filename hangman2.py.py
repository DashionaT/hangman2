#Hangman
#Dashiona T.
import os
import random

def header():
    pass

def splash_screen():
    path = "art"

    files = 'art/splashscreen.txt'

    with open(files, 'r') as f:
        lines = f.read()

    print(lines)


def show_credits():
    path = "art"

    files = 'art/ending.txt'

    with open(files, 'r') as f:
        lines = f.read()

    print(lines)

def get_name():
    print("What is your name?")
    name = input()
    print("It is nice to meet you, " + name + ". Please choose a category.")
    return name
     
def get_puzzle():
    
    path = "data"
    funz_file = ""
    file_names = os.listdir(path)

    for i, f in enumerate(file_names):
        this_file = f
        with open(path + "/" + this_file, 'r') as f:
            beginning_lines = f.read().splitlines()
        category_name = beginning_lines[0]
        print(str(i + 1) + " " + category_name)

    choice = input('pick one ')
    choice = int(choice)-1

    file = path + "/" + file_names[choice]


    with open(file, 'r') as f:
        lines = f.read().splitlines()

    print(lines)

    puzzle = random.choice( lines[1:] )

    return puzzle


def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess(name):
    letter = input("Guess a letter " + name + ": ")
    return letter

def display_board(solved):
    print(solved)

def show_result(strikes, limit):

    if strikes == limit:
        print ("You lose " + name + "!")
        result = 1
        gameover = 1

    else:
        print("You Win " + name + "!")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision= decision.lower()
        
        print("")
        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play(name):
    puzzle = get_puzzle()

    guesses = ""
    solved = "-" * len(puzzle)

    strikes = 0
    limit = 6
    result = 0
    gameover = 0
    
    display_board(solved)
    
    while solved != puzzle:
        letter = get_guess(name)

        if letter not in puzzle:
            strikes += 1
            if strikes == limit:
                return print ("You ran out of tries... You lose " + name + "!")

            
        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved)

    show_result(0,6)

header()
splash_screen()   
name = get_name()
playing = True

while playing:
    play(name)
    playing = play_again()

show_credits()
