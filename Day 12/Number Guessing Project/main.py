from art import logo
import random

LEVEL_EASY_TURNS = 10
LEVEL_HARD_TURNS = 5

def set_turns():
    """ Returns the correct number of turns based on a user input"""
    level_selection = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level_selection == "easy":
        attempts = LEVEL_EASY_TURNS
    else:
        attempts = LEVEL_HARD_TURNS
    return attempts

def get_guess():
    """Prompts the user for a number and returns as an integer. Continues to check if the input is invalid"""
    while True:
        try:
            return int(input("Make a guess: "))
        except ValueError:
            print("Please enter a number.")

#6 Guess function - make a guess, too low / too high / you got it
def check_guess(guess, random_number):
    """ Prints out the hint based on the last guess"""
    if guess < random_number:
        print(f"Too Low. \nGuess again.")
    else:
        print(f"Too High. \nGuess again.")

def game():
    # 1 import and print logo
    print(logo)

    # 2 Print Welcome message
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # 3 Set random number to a variable (1-100)
    random_number = random.randint(1, 100)

    # 4 Ask easy / hard - set turns to a variable (5 - hard, 10 - easy)
    attempts = set_turns()

    guess = 0
    #5 Loop - you have {turns} attempts / run guess function while answer is wrong
    while guess != random_number:
        print(f"You have {attempts} attempt(s) remaining to guess the number.")
        guess = get_guess()
        if guess == random_number:
            print(f"You got it! The answer was {random_number}.")
            return
        check_guess(guess, random_number)
        attempts = attempts - 1
        if attempts == 0:
            print(f"You lose! The number was {random_number}.")
            return

game()
