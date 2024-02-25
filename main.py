from art import logo
from random import choice

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    return card


def print_scores(user, score1, pc, score2):
    print(f"Your final hand: {user}, final score: {score1}\n"
          f"Computer's final hand: {pc}, computer's final score: {score2}")

def score_calculator(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        score -= 10
        cards.remove(11)
        cards.append(1)
    return score

def black_jack():
    start = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
    user_cards = []
    computer_cards = []
    should_continue = True
    if start == 'y':
        print(logo)
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        while should_continue:
            user_cards.append(deal_card())
            if score_calculator(computer_cards) < 17:
                computer_cards.append(deal_card())
            user_score = score_calculator(user_cards)
            computer_score = score_calculator(computer_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")
            if user_score > 21:
                should_continue = False
                print_scores(user_cards, user_score, computer_cards, computer_score)
                print("You went over. You lose.😭")

            elif user_score == 21 and len(user_cards) == 2:
                should_continue = False
                print_scores(user_cards, user_score, computer_cards, computer_score)
                print("BLACK JACK!🤯")

            elif computer_score == 21 and len(computer_cards) == 2:
                should_continue = False
                print_scores(user_cards, user_score, computer_cards, computer_score)
                print("opponent BLACK JACK!🤯")

            elif computer_score > 21:
                should_continue = False
                print("Opponent went over. You win!😎")
                print_scores(user_cards, user_score, computer_cards, computer_score)

            else:
                if input("Type 'y' to get another card or 'n' to pass: ").lower() == 'n':
                    if user_score > computer_score:
                        print("You win!😎")
                    else:
                        print("You lose.😭")
                    print_scores(user_cards, user_score, computer_cards, computer_score)
                    should_continue = False
        black_jack()
    else:
        print("You typed the wrong word or else you dont wanna play...try again")

black_jack()

























