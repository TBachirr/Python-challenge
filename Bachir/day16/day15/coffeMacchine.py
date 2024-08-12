Menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def check_resources(drink):
    for item in drink["ingredients"]:
        if drink["ingredients"][item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def choice(drink):
    for item in drink["ingredients"]:
        resources[item] -= drink["ingredients"][item]
    resources["money"] += drink["cost"]
    print(f"Here is your {drink_name} ☕. Enjoy!") 

def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def make_coffee(drink):
    if check_resources(drink):
        payment = process_coins()
        if payment >= drink["cost"]:
            change = round(payment - drink["cost"], 2)
            print(f"Here is ${change} in change.")
            choice(drink)
        else:
            print("Sorry, that's not enough money. Money refunded.")

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

while True:
    drink_name = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if drink_name == "report":
        report()
    elif drink_name in Menu:
        make_coffee(Menu[drink_name])
    else:
        print("Invalid input. Please choose espresso, latte, cappuccino, or type 'report'.")
