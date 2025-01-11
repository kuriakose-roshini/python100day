def find_highest_bidder(bidder_dictionary):
  winner = ""
  highest_bid = 0
  max(bidding_dictionary)
  for bidder in bidding_dictionary:
    bid_amount = bidding_dictionary[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder

print(f"the winner is {bidder} with a bid of {highest_bid})

bid{}
continue_bidding = True
while continue_bidding = True:
  name = input("Enter your name")
  price = int(input("Enter your bidding price:"))
  bid[name] = price
  should_continue = input("Are there any other bidders? Type yes or no")
  if should_continue == "no":
    continue_bidding = False
    find_highest_bidder(bid)
  elif should_continue == "yes":
    print("\n" * 20)
    continue_bidding = True
