############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def start_game():
    print(logo)

    user_cards = []
    computer_cards = []

    user_score = 0
    computer_score = 0
    game_is_over = False

    def deal_card(player_cards):
        sum_cards = sum(player_cards)
        random_card = random.choice(cards)

        if sum_cards == 0:
            return random_card
        elif sum_cards + random_card > 21:
            if random_card == 11:
                return 1
            else:
                return random_card
        else:
            return random_card

    def calculate_score(cards):
        return sum(cards)

    for _ in range(2):
        user_cards.append(deal_card(user_cards))
        computer_cards.append(deal_card(computer_cards))

    #  Calculate score to dermine winner
    def calculate_winner(user_score, computer_score):
        if user_score > 21 and computer_score > 21:
            return "You went over. You lose 😤"

        if user_score == computer_score:
            return "Draw 🙃"
        elif computer_score == 0:
            return "Lose, opponent has Blackjack 😱"
        elif user_score == 0:
            return "Win with a Blackjack 😎"
        elif user_score > 21:
            return "You went over. You lose 😭"
        elif computer_score > 21:
            return "Opponent went over. You win 😁"
        elif user_score > computer_score:
            return "You win 😃"
        else:
            return "You lose 😤"

    while not game_is_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 21 or computer_score == 21 or user_score > 21:
            game_is_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card(user_cards))
            else:
                game_is_over = True

    # Choose computer cards
    while computer_score < 17:
        computer_cards.append(deal_card(computer_cards))
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(calculate_winner(user_score, computer_score))


while input(f"Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    start_game()
