from replit import clear
from art import logo

continue_auction = True
AllBids = {"names": [], "bids": []}

while continue_auction:
  
  print(logo)
  print("Welcome to the Secret Auction Program.")
  name = input("What is your name? ")
  bid = input("What is your bid? ")
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






    

#HINT: You can call clear() to clear the output in the console.