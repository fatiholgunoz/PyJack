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

import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = []
dealer_hand = []
#global ace_index = 0
get_card = "y"

print(art.logo)
print("Welcome to PyJack, your favourite blackjack game!")

def new_card():
  drawn_card = random.choice(cards)
  return drawn_card

def has_ace(hand):
  global ace_index
  for card_num in range(len(hand)):
    if hand[card_num-1] == 11:
      ace_index = card_num-1
      return True 
    else:
      return False
      
for times in range(2):
  user_hand.append(new_card())
  dealer_hand.append(new_card())

if sum(dealer_hand) == 21:
  print("\nThe dealer wins with a blackjack.")
  get_card = "n"
elif sum(user_hand) == 21:
  print("\nYou win with a blackjack!")
  get_card = "n"

if sum(dealer_hand) > 21 and has_ace(dealer_hand):
  dealer_hand[ace_index] = 1
  print("TO BE REMOVED: Dealer's ace was set to 1")        #TO BE REMOVED
if sum(user_hand) > 21 and has_ace(user_hand):
  user_hand[ace_index] = 1
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
    elif sum(user_hand) > 21 and has_ace(user_hand):
      user_hand[ace_index] = 1
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
















##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt
##################### \ ##################### \ ##################### 

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

