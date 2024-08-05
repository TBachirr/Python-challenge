print("Welcome to pizza deliveries!")
pizza_size = input("What pizza size do you want ? S M or L : ")

if pizza_size == "S":
    price = 15
    print("You choosed a Small Pizza")
elif pizza_size == "M":
    price = 20
    print("You choosed a Medium Pizza")
elif pizza_size == "L":
    price = 25
    print("You choosed a Large Pizza")
else:
    print("Choose a valid size.")
    
add_pepperoni = input("Do you want Pepperoni ? Y or N : ")

if add_pepperoni == "Y":
    if pizza_size == "S":
        price += 2
        print(f"You choosed to add Pepperoni, your bill is now {price}")    
    elif  pizza_size == "M" or "L":
        price += 3
        print(f"You choosed to add Pepperoni, your bill is now {price}")    
    else:
        print("You choosed not to add Pepperoni")    
else:
    print("You choosed not to add Pepperoni")
    
    
extra_cheese = input("Do you want extra Cheese ? Y or N : ")

if extra_cheese == "Y":
    price += 1
    print(f"You choosed to add extra cheese, You have to pay : {price}")
else:
    print(f"You choosed not to add cheese, You will have to pay {price}")