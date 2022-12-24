############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import art
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def new_card():
  drawn_card = random.choice(cards)
  return drawn_card

def play_game():
  print(art.logo)
  print("Welcome to PyJack, your favourite blackjack game!")  
  
  user_hand = []
  dealer_hand = []
  get_card = "y"
  
  for times in range(2):
    user_hand.append(new_card())
    dealer_hand.append(new_card())
  
  if sum(dealer_hand) == 21:
    print("\nThe dealer wins with a blackjack.")
    get_card = "n"
  elif sum(user_hand) == 21:
    print("\nYou win with a blackjack!")
    get_card = "n"
  
  if sum(dealer_hand) > 21 and 11 in dealer_hand:
    dealer_hand.remove(11)
    dealer_hand.append(1)

  if sum(user_hand) > 21 and 11 in user_hand:
    user_hand.remove(11)
    user_hand.append(1)
    print("User's ace was set to 1")
  
  print(f"\nYour cards: {user_hand}, current score = {sum(user_hand)}")
  if get_card == "y":
    print(f"Dealer's first card: {dealer_hand[0]}")
  
  while sum(user_hand) < 22 and get_card == "y":
    get_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if get_card == "y":
      user_hand.append(new_card())
      if sum(user_hand) == 21:
        get_card = "n"
        print("\nYou win with a score of 21.")
      elif sum(user_hand) > 21 and 11 in user_hand:
        user_hand.remove(11)
        user_hand.append(1)
        print("\nUser's ace was set to 1")
      elif sum(user_hand) > 21:
        get_card = "n"
        print("\nYou went over, the dealer wins.")
        
      print(f"\nYour cards: {user_hand}, current score = {sum(user_hand)}")
      if get_card == "y":
        print(f"Dealer's first card: {dealer_hand[0]}")
    elif get_card == "n":
      print(f"\nYour cards: {user_hand}, final score = {sum(user_hand)}")
  
  while sum(dealer_hand) < 17 and sum(user_hand) < 21:
    dealer_hand.append(new_card())
  
  print(f"Dealer's cards: {dealer_hand}, dealer score = {sum(dealer_hand)}")
  
  if sum(dealer_hand) > 21:
    print("Dealer went over, you win!")
  elif sum(dealer_hand) == 21:
    print("Dealer wins with a score of 21.")
  
  if sum(user_hand) < 21 and sum(dealer_hand) < 21:
    if sum(user_hand) < sum(dealer_hand):
      print("\nDealer wins.")
    elif sum(dealer_hand) < sum(user_hand):
      print("\nYou win!")
    elif sum(user_hand) == sum(dealer_hand):
      print("\nIt's a draw.")

while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()