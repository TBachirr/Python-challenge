import random

def initialize_game():
    print("Welcome to Guessing Number Game")
    number = random.randint(1, 100)
    return number

def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    else:
        print("Invalid choice. Defaulting to 'easy'.")
        return 10

def play_game(number, chances):
    print("Guess a number (between 1 and 100):")
    num = 0
    while num < chances:
        guess = int(input())
        if guess == number:
            print("Congratulations! You won")
            break
        elif guess < number:
            print("Your guess was too low: Guess a number higher than", guess, ". You have", chances - num - 1, "chances left.")
        else:
            print("Your guess was too high: Guess a number lower than", guess, ". You have", chances - num - 1, "chances left.")
        num += 1
    
    if num == chances:
        print("YOU LOSE!!! The number was", number)


number = initialize_game()
chances = choose_difficulty()
play_game(number, chances)
