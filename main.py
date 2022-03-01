from replit import clear
from art import logo

continue_auction = True
AllBids = {"names": [], "bids": []}

while continue_auction:
  
  print(logo)
  print("Welcome to the Secret Auction Program.")
  name = input("What is your name? ")
  bid = int(input("What is your bid? "))
  more_bids = input("Are there any other bidders? Type 'yes' or 'no'. ")


  def add_bidder(name, bid):
    """adds bidder name and bid amount to dictionary"""
    AllBids["names"].append(name)
    AllBids["bids"].append(bid)
    
  add_bidder(name, bid)

  if more_bids == 'yes':
    clear()
  else:
    continue_auction = False

def find_winner():
  max_bid = max(AllBids["bids"])
  winning_index = AllBids["bids"].index(max_bid)
  winner_name = AllBids["names"][winning_index]
  winner_bid = AllBids["bids"][winning_index]
  print(f"The winner is {winner_name} with a bid of ${winner_bid}!")

find_winner()


    

#HINT: You can call clear() to clear the output in the console.