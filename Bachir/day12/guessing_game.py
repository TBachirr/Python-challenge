import random
from art import logo

print(logo)
print("""Welcome to the Guessing Game !
I am thinking of a number between 1 and 100.""")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard' :")

attempt = 0

if difficulty == "easy":
    attempt = 10
elif difficulty == "hard":
    attempt = 5

def game():
    global attempt
    number_to_guess = random.randint(1, 100)
    for i in range(attempt):
        guess = int(input("Make a guess: "))
        if guess == number_to_guess:
            print(f"You got it right! The number was {number_to_guess}")
            break
        else:
            if guess > number_to_guess:
                print("Too high")
            else:
                print("Too low")
            attempt -= 1
            print(f"You have {attempt} attempts remaining to guess the number.")
    if attempt == 0:
        print(f"You lose! The number was {number_to_guess}")


if difficulty == 'easy' or difficulty == 'hard':
    game()
else:
    print("You need to enter either easy or hard")
