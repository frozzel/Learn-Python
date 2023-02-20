
from art import logo_black_jack
from replit import clear
import random

def calculate_score(cards):
  """This function takes a lisk of cards and calculates a score"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
  
def compare (user_score, computer_score) :
  if user_score ==  computer_score:
    return "Draw !"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack!"
  elif user_score == 0:
    return "You Win, Blackjack"
  elif user_score > 21:
    return "You went over, You Lose"
  elif computer_score > 21:
    return "Computer went over 21, You Win"
  elif user_score > computer_score:
    return "You Win"
  else: 
    return "You Lose"
 
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
  
def play_black_jack():
  print(logo_black_jack)
  user_cards = []
  computer_cards = []
  game_over = False
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computers first Card is: {computer_cards[0]}")
    
    if user_score==0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      user_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      if user_deal == 'y':
        user_cards.append(deal_card())
      else:
        game_over = True
  
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computers final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
  
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
  clear()
  play_black_jack()
