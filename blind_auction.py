from blind_auction_art import logo
import os
print(logo)
bid = {}
auction_finished = False

def find_highest_bidder(bidding_list):
    highest_bid = 0
    bidder = ""


    for bidder in bidding_list:
        bidding_amount = bidding_list[bidder]
        if bidding_amount > highest_bid:
            highest_bid = bidding_amount
            winner = bidder
    print(f"the highest bidder is {winner} with a bidding of ${highest_bid}")    

while not auction_finished:
    name = input("Enter the name of bidder: ")
    price = int(input("Enter your price: $"))
    bid[name] = price
    cnt = input("if you want to continue type yes or else no: to discontinue:")
    if cnt == "yes":
        os.system("cls")
        
    elif cnt == "no":
        auction_finished = True
        find_highest_bidder(bid)