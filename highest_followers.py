#imports
from game_data import data
import random 
from art import logo_followers, vs
from replit import clear
#functions
def play_game():
  def random_data():
    """Function to Create Random Choice"""
    list = random.randint(0, 49)
    card = data[list]
    name1 = card["name"]
    description1 = card["description"]
    country1 = card["country"]
    followers1 = card['follower_count']
    return [name1, description1, country1, followers1]
 
  #code
  print(logo_followers)
  score = 0
  A = random_data()
  B = random_data()
  winning = True
  while winning:
    print(f"Compare A: {A[0]}, a {A[1]}, from {A[2]}. {A[3]} million followers")
    print(vs)
    print(f"Compare B: {B[0]}, a {B[1]}, from {B[2]}. {B[3]} million followers")
    test = input("Who has more followers? Type 'A' or 'B': ").upper()
    if test == "A":
      comp1 = A[3]
      comp2 = B[3]
    else:
      comp1 = B[3]
      comp2 = A[3]
    if comp1 >= comp2:
      score += 1
      clear()
      print(logo_followers)
      print(f"You're right! Current score: {score}.")
      if test == "A":
        A  = A
        B = random_data()
      else:
        A = B
        B = random_data()
    else:
      winning = False
      clear()
      print(logo_followers)
      print(f"Sorry, that's wrong. Final score: {score}")

play_game()
run = input("Play Again Y/N  ").lower()
if run == 'y':
  play_game()
else:
  print("Thanks for Playing Good Bye!")