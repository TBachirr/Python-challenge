import random 

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

user_choice = int(input("Make a choice, 0 for rock, 1 for paper and 2 for scissors. \n"))
computer_choice = random.randint(0, 2)
print(f"Computer choose {computer_choice}")

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")