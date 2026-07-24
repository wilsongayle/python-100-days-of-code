from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Returns a random card"""
    return random.choice(cards)

def total_cards(arr):
    """Totals the cards in the provided array. Subtracts 10 if an ace is present and the total is over 21."""
    total = 0
    ace_cards = []
    for card in arr:
        if card == 11:
            ace_cards.append(10)
        total += card
    while total > 21 and ace_cards:
        total -= ace_cards.pop()
    return total

def calculate_result(my_cards, computer_cards, my_natural, computer_natural):
    """Calculates the final result at the end of the game. Returns a string of the result."""
    computer_score = total_cards(computer_cards)
    my_score = total_cards(my_cards)
    print(f"\tYour final hand: {my_cards}, final score: {my_score}")

    if computer_natural or my_natural:
        print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")
        if computer_natural and my_natural:
            return "Draw"
        elif my_natural:
            return "You got a blackjack! You win!"
        elif computer_natural:
            return "Computer got a blackjack. You lose!"

    if my_score > 21:
        return "You went over. You lose!"
    else:
        while computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = total_cards(computer_cards)
        print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")

    if computer_score == my_score:
        return "Draw"
    elif computer_score > 21:
        return "The computer went over. You win!"
    elif computer_score > my_score:
        return "You lose"
    else:
        return "You win!"

def print_table(my_cards, computer_cards):
    """Prints the user's and the computer's current cards and score."""
    print(f"\tYour cards: {my_cards}, current score: {total_cards(my_cards)}")
    print(f"\tComputer's first card: {computer_cards[0]}")

def blackjack():
    """One game of blackjack."""
    my_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    my_score = total_cards(my_cards)

    print("\n" * 25)
    print(logo)

    my_turn = True

    my_natural = my_score == 21
    computer_natural = total_cards(computer_cards) == 21

    if my_natural or computer_natural:
        my_turn = False

    while my_turn:
        print_table(my_cards, computer_cards)
        if my_score > 21:
            my_turn = False
        else:
            take_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if take_another_card == 'y':
                my_cards.append(deal_card())
                my_score = total_cards(my_cards)
            else:
                my_turn = False

    print(calculate_result(my_cards, computer_cards, my_natural, computer_natural))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    blackjack()