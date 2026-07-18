from art import logo

print(logo)
print("Welcome to the secret auction program.")
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

bids = {}
more_bidders = True

while more_bidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    done = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if done == "no":
        more_bidders = False
    print("\n" * 20)

def print_winner(bids_dictionary):
    winner = ''
    winning_bid = 0
    for bidder_name in bids_dictionary:
        bid_amount = bids_dictionary[bidder_name]
        if bid_amount > winning_bid:
            winning_bid = bid_amount
            winner = bidder_name

    print(f"The winner is {winner} with a bid of ${winning_bid}")

print_winner(bids)