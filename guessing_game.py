from replit import clear
from art import logo_guess
import random

def guessing_game():
  print(logo_guess)
  
  ans = random.randint(1, 100)
  
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  #Testing
  
  print(f"correct ans: {ans}")
  
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
  if difficulty == "easy":
    attempt = 10
  elif difficulty == "hard":
    attempt = 5
  else:
    print("Please chose a difficulty level")
  guessing = True
  while guessing:
    if attempt > 0:
      print(f"You have {attempt} attempts remaining to guess the number.")
      guess = int(input("Make a guess: "))
      if ans == guess:
        guessing = False
        print(f"You got it! The answer was {ans}.")
      elif ans > guess:
        attempt -= 1
        print("To Low")
      elif ans < guess:
        attempt -= 1
        print("To High")
    else:
      guessing = False
      print("You've run out of guesses, you lose.")


guessing_game()

if input("Play Again Y/N  ").lower() == 'y':
  clear()
  guessing_game()
else:
  print("Good Bye! Thanks for playing!")

## There answer 
  '''from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()

'''