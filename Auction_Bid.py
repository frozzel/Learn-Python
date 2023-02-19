from replit import clear
from art import logo_auction

print(logo_auction)
print("Welcome to Your Silent Auction")

auction  = {}
keep_bidding = True

def find_highest_bid(record):
  highest_bid = 0
  winner = ""
  for bidder in record:
    bid_amount = record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder 
  print(f"The winnier is {winner} with a bid of ${highest_bid}")
      


while keep_bidding:
  name = input("What is your name?:  ")
  bid = int(input("What's your bid?:  $"))
  auction[name] = bid
  run = input("Are there other bidders? Y/N  ").lower()
  if not run  == "y":
    keep_bidding = False
    find_highest_bid(auction)
  else:
    clear()
    