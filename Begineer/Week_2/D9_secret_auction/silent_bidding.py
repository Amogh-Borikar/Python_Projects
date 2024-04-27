import os

from Art import logo

print(logo)

bidders = {}
next_bidder = "yes"
while next_bidder == "yes":
  name = input("What is your name? : ")
  bid = int(input(f"What is your bid {name}? Type in $: "))
  bidders[name] = bid
  next_bidder = input("Are there any other bidders? Type 'yes' or 'no'.")
  
  if next_bidder == "yes":
    # Clear the terminal in Windows
    if os.name == 'nt':
      os.system('cls')
    # Clear the terminal in Linux and macOS
    else:
      os.system('clear')
  
  else:
    # Clear the terminal in Windows
    if os.name == 'nt':
      os.system('cls')
    # Clear the terminal in Linux and macOS
    else:
      os.system('clear')
    
    max_bid = 0
    winner = ""
    
    for bidder in bidders:
      if bidders[bidder] > max_bid:
        max_bid = bidders[bidder]
        winner = bidder
    print(f"The winner is {winner} with a bid of ${max_bid}")