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
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   
print(logo)

# deal_card() function that uses the List 'cards' to return a random card.
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

# calculate_score() takes a list of player cards as input.
def calculate_score(player_cards):
  if len(player_cards) == 2 and (player_cards) == 21:
    return 0 # 0 represents a BlackJack
    
  if sum(player_cards) > 21 and 11 in player_cards:
    player_cards.remove(11)
    player_cards.append(1)
    
  return sum(player_cards)

# compare() takes user_score and computer_score and checks whether the user_score is higher or not
def compare(user_score, computer_score):
  if user_score == computer_score:
    return 'Draw'
  elif computer_score == 0:
    return 'Computer has BlackJack!!!!!'
  elif user_score == 0:
    return 'You Won BlackJack!!!!!'
  elif user_score > 21:
    return 'You went over 21. You lose!!!!!'
  elif computer_score > 21:
    return 'Computer went over 21. You Win!!!!!'
  elif user_score > computer_score:
    return 'You Win!!!!!'
  else:
    return 'You Lose!!!!!'
user_cards = []
computer_cards = []
is_game_over = False

# Deal the user and computer 2 cards each using deal_card() and append().
for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

while not is_game_over:
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  
  print(f'user cards {user_cards},  user score : {user_score}')
  print(f'computer\'s first card : {computer_cards[0]}')

  if computer_score == 0 or user_score == 0 or user_score > 21:
    is_game_over = True
  else:
      another_card = input("Do you want to draw another card. Type 'Yes' or 'no': \n ---> ").lower()
      if another_card == 'yes':
        user_cards.append(deal_card())
      else:
        is_game_over = True

while computer_score != 0 and computer_score < 17:
  computer_cards.append(deal_card())
  computer_score = calculate_score(computer_cards)
  
print(f"Final Computer cards: {computer_cards} Computer Score: {computer_score}")
print(f"Final User cards: {user_cards} User Score : {user_score}")

print(compare(user_score, computer_score))
