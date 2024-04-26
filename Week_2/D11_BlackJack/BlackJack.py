import random
import os
from art import logo

def deal_card():
    """deals a random card."""
    card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(card_list)

def calculate_score(list):
    """returns calculated score for the cards according to the rules of BlackJack."""
    score = sum(list)
    if len(list) == 2 and 11 in list and 10 in list:
        return 0
    elif 11 in list and score > 21:
        list.remove(11)
        list.append(1)
        score = sum(list)
        return score
    else:
        return score

def compare(dealer_score, user_score):
    if user_score == dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "You lose, Dealer has BlackJack!"
    elif user_score == 0:
        return "You win with a BlackJack!!"
    elif user_score > 21:
        return "You lose, you went over 21!"
    elif dealer_score > 21:
        return "You win, dealer went over 21!"
    elif user_score > dealer_score:
        return "You win!"
    else:
        return "You Lose!"

def play_blackjack():

    print(logo)

    dealer_cards = []
    user_cards = []
    is_game_over = False
    
    for i in range(2):
        dealer_cards.append(deal_card())
        user_cards.append(deal_card())

    print(f"dealer's first card is {dealer_cards[0]}")

    while not is_game_over:

        dealer_score = calculate_score(dealer_cards)
        user_score = calculate_score(user_cards)

        print(f"your current hand is {user_cards}, with total score of {user_score}") 

        if dealer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_choice = input("Draw another card? Type 'y' or 'n' :")
            if user_choice == "y":
                user_next_card = deal_card()
                user_cards.append(user_next_card)
                user_score = calculate_score(user_cards)
                print(f"You got {user_next_card}")
            else:
                is_game_over = True

    while dealer_score < 17 and dealer_score != 0 :
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print("""
          
          
          """)
    print(f"Your final hand is {user_cards}, with total score of {user_score}.")
    print(f"Dealer's final hand is {dealer_cards}, with total score of {dealer_score}.")
    print(compare(dealer_score, user_score))
    print("""
          
          """)

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == "y":
    # Clear the terminal in Windows
    if os.name == 'nt':
      os.system('cls')
    # Clear the terminal in Linux and macOS
    else:
      os.system('clear')    
    play_blackjack()