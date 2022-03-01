from replit import clear
from art import logo

continue_auction = True
AllBids = {}

while continue_auction:
  
  print(logo)
  print("Welcome to the Secret Auction Program.")
  name = input("What is your name? ")
  bid = input("What is your bid? ")
  more_bids = input("Are there any other bidders? Type 'yes' or 'no'. ")


  def add_bidder(name, bid):
    """adds bidder name and bid amount to dictionary"""
    AllBids[name] = bid
    
  add_bidder(name, bid)

  if more_bids == 'yes':
    clear()
  else:
    continue_auction = False

bid_list = []
for key in AllBids:
  AllBids[key] += bid_list

winning_bid = max(bid_list)
winning_name = 



    

#HINT: You can call clear() to clear the output in the console.