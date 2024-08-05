print("Welcome to Treasure Island!")
print("Your mission is to find the treasure")
dir=input("You are at a crossroads,which direction do you want to go in?left or right\n")


if(dir=="right"):
    print("Game over")

elif(dir =="left"):
    action=input("You want to swim or wait?\n")
    if(action=="swim"):
        print("Game over")

    elif(action=="wait"):
        door=input("Which door do you choose?red,blue or yellow\n")
        if(door=="blue" or door=="red"):
            print("Game over")

        elif(door=="yellow"):
            print("Congrats...you win!!!")

        else:
            print("Choose red,blue or yellow")

    else:
        print("Choose action as swim or wait only")

else:
    print("Sorry choose left or right only")