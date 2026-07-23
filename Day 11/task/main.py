from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

playing_game = True

def add_random_card(arr):
    random_card = random.choice(cards)
    arr.append(random_card)

def total_cards(arr):
    total = 0
    ace_cards = []
    for card in arr:
        if card == 11:
            ace_cards.append(10)
        total += card
    while total > 21 and ace_cards:
        total -= ace_cards.pop()
    return total


def blackjack():
    my_cards = []
    computer_cards = []
    my_score = 0

    def print_table():
        print(f"\tYour cards: {my_cards}, current score: {my_score}")
        print(f"\tComputer's first card: {computer_cards[0]}")

    def calculate_result():
        computer_score = total_cards(computer_cards)
        print(f"\tYour final hand: {my_cards}, final score: {my_score}")

        if my_score > 21:
            return "You went over. You lose!"
        else:
            while computer_score < 17:
                add_random_card(computer_cards)
                computer_score = total_cards(computer_cards)
            print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")

        if computer_score == 21:
            return "Computer got a blackjack. You lose!"
        if computer_score > 21:
            return "The computer went over. You win!"
        elif computer_score == my_score:
            return "Draw"
        elif computer_score > my_score:
            return "You lose"
        else:
            return "You win!"


    print("\n" * 25)
    print(logo)

    add_random_card(my_cards)
    add_random_card(my_cards)
    my_score = total_cards(my_cards)
    add_random_card(computer_cards)
    add_random_card(computer_cards)

    my_turn = True

    if total_cards(computer_cards) == 21:
        my_turn = False

    while my_turn:
        print_table()
        if my_score > 21:
            print("You went over. You lose!")
            my_turn = False
        else:
            take_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if take_another_card == 'y':
                add_random_card(my_cards)
                my_score = total_cards(my_cards)
            else:
                my_turn = False

    print(calculate_result())


while playing_game:
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if want_to_play == 'y':
        blackjack()
    else:
        playing_game = False