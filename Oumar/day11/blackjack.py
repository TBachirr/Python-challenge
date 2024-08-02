import random
print("WELCOME TO BLACK JACK")
def play_game():

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards)) 

    game_over = False

    while not game_over:

        user_score = sum(user_cards)
        computer_score = sum(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 21 or computer_score == 21:
            game_over = True

        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")

            if user_should_deal == "y":
                user_cards.append(random.choice(cards))

            else:
                game_over = True

    while computer_score != 21 and computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_score = sum(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    if computer_score == 21:
        print("Lose, opponent has Blackjack")

    elif user_score == computer_score:
        print("Draw")

    elif computer_score > 21:
        print("You went over. You lose")

    elif user_score > computer_score:
        print("You win")

    else:
        print("You lose")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
