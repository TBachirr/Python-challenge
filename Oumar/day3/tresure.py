print('''
  _______
 / ______|
| |_____| _______  _______  _______  __
| |    | |       ||       ||       ||  |
| |    | |____   | |____   |   _   ||  |
| |    |_____|  | |_____|  |  | |  ||  |    
 \______|      |$|      |  |  |_|  ||__|
               |___|      |_________|
''')

print("Wwlcome to Treasure Island.")
print("Your mission is to find the treasure.")
path = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right'").lower()
if path == "left":
    path = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.").lower()
    if path == "wait":
        path = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower()
        if path == "red":
            print("It's a room full of fire. Game Over.")
        elif path == "yellow":
            print("You found the treasure! You Win!")
        elif path == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")