#SECRET AUCTION
#Import modules and print ASCII art
from replit import clear
from art import logo
print(logo)

#Define empty dictionary
auction = {}

#Run the auction...
end_of_auction = False

while not end_of_auction:
    name = input("What is your name? ")
    bid = int(input("What is your bid? £"))
    #Add name (key) and bid (value) to dictionary
    auction[name] = bid

    #Any more bidders?
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if more_bidders =="yes":
        clear()
    elif more_bidders =="no":
        clear()
        end_of_auction = True

#Determine the winner
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of £{highest_bid}!")

find_highest_bidder(auction)

#Other possible method for finding the winner and highest_bid
#winner = max(auction, key=auction.get)
#highest_bid = auction[winner]