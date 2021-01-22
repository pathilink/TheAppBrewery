from os import system, name
from art_auction import logo

def clear():
    # for Windows
    if name == 'nt':
        _ = system("cls")
    # for mac and linux (os.name is 'posix')
    else:
        _ = system("clear")

print(logo)
print("Welcome to the secret auction program.")

bids = {}

def highest_bid(bids_dict):
    higher_value = 0
    winner = ""
    for bidder in bids_dict:
        auction_bid = bids_dict[bidder]
        if auction_bid > higher_value:
            higher_value = auction_bid
            winner = bidder 
    print(f"The winner is {winner} with a bid of ${higher_value}.")


question = True
while question:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    bidders = input("Are there any others bidders? Type 'yes' or 'no'.\n")
    if bidders == 'yes':
        clear()   # https://www.geeksforgeeks.org/clear-screen-python/
    else:
        question = False
        highest_bid(bids)
