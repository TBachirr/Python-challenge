from art import logo, vs
from data import datas
import random

print(logo)
print("Welcome to the Higher or Lower Game")



def comparation(guess, a, b):
    if guess == "a":
        return a["follower_count"] > b["follower_count"]
    elif guess == "b":
        return b["follower_count"] > a["follower_count"]
    else:
        print("Wrong input")
        return False

def game():
    loose = False
    score = 0
    choice = random.choice(datas)
    while not loose:
        a = choice
        b = random.choice(datas)
        while a == b:
            b = random.choice(datas)
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        print(vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if comparation(guess, a, b):
            score += 1
            print(f"You're right! Current score: {score}")
            choice = b
        else:
            loose = True
            print(f"Sorry, that's wrong. Final score: {score}")

game()

    