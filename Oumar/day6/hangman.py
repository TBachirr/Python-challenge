import random
print("Wellcome to Hangman")
name = input("Enter your name: ")
print("Good luck ! Guess the language", name.capitalize())
mots = ['python', 'java', 'kotlin', 'javascript', 'rust', 'golang', 'csharp', 'php', 'dart', 'ruby', 'swift' ]
devine = random.choice(mots)
chances = 5
dev =["_"] * len(devine)
print("".join(dev),end="")
while chances > 0 and "_" in dev:
    guess = input("\nGuess a letter: ").lower()
    if guess in devine:
        for i in range(len(devine)):
            if devine[i] == guess:
                dev[i]=guess       
    else:
        print("Wrong guess")
        chances -= 1
    print("\nYou have", chances, "more guesses")
    print("".join(dev))
    if "_" not in dev:
        print("You win")
        break
    elif chances == 0:
        print("You lose")
        break





