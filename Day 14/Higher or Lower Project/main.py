# import art and data (make sure you can print data)
import random

from art import logo, vs
from game_data import data

# create a variable to save the score
# variable for A and B - variable for still_playing
# create the game as a function

# select a random entry for A
# select a random entry for B
# (B becomes A - if A is '', select random)

def format_data(account):
    """Returns a formatted string of account data"""
    return f"{account['name']}, a {account['description']}, from {account['country']}"

def get_guess():
    """Prompts the user to enter a or b as a guess, loops until correct guess type is entered."""
    valid_guess = False
    guess = None
    while not valid_guess:
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess != 'a' and guess != 'b':
            print("Please enter 'a' or 'b'")
        else:
            valid_guess = True
    return guess

def is_correct_guess(guess, account_a, account_b):
    """Takes the guess and the accounts. Returns if the guess is correct that the follower count is more."""
    if account_a['follower_count'] > account_b['follower_count']:
        return guess == 'a'
    else:
        return guess == 'b'

def play():
    """Plays the game"""
    score = 0
    account_a = random.choice(data)
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    still_playing = True
    winning = False

    while still_playing:
        # Print starting setup:
        # - Logo art
        # - Compare A: {Name}, a {description}, from {country}.
        # - Empty Line
        # - Vs art
        # - Against B: {Name}, a {description}, from {country}.

        print("\n" * 26)
        print(logo)
        if winning:
            print(f"You're right! Current score: {score}.")
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        # input: (convert to lower case / handle invalid entries)
        # - Who has more followers? Type 'A' or 'B':
        # - compare A {follower_count} with B {follower_count}
        #    - if input = A and A > B or input = B and B > A
        guess = get_guess()

        # If right:
        # - increment score
        # - Clear screen
        # - Reprint starting setup with new line after logo:
        #   - You're right! Current score: {}.
        # - winner becomes A
        still_playing = is_correct_guess(guess, account_a, account_b)
        if still_playing:
            winning = True
            score += 1
            if guess == 'b':
                account_a = account_b
            account_b = random.choice(data)
            while account_a == account_b:
                account_b = random.choice(data)

        # - Logo art
        # - You're right! Current score: {}.
        # - Compare A: {Name}, a {description}, from {country}.
        # - Empty Line
        # - Vs art
        # - Against B: {Name}, a {description}, from {country}.

    # If wrong:
    # - Clear screen
    # - Print:
    #   - Logo
    #   - Sorry, that's wrong. Final score: {}
    print("\n" * 26)
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")

play()
