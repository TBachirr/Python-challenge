print("Welcome to the Auction House")
from replit import clear # type: ignore

bid = {}

while True:

    name = input("Enter your name: ")

    bid_price = int(input("Enter your bid price: "))

    bid[name] = bid_price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no' ")

    if should_continue == "no":
        break

    elif should_continue == "yes":
        
        clear()
        continue

    else:
        print("Invalid input")

print(bid)

highest_bid = 0
winner = ""

for key in bid:
    if bid[key] > highest_bid:
        highest_bid = bid[key]
        winner = key

print(f"The winner is {winner} with a bid of ${highest_bid}")

