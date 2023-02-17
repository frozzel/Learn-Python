def hangman():
  from replit import clear
  import random
  from hangman_words import word_list
  from hangman_art import logo, stages
  
  chosen_word = random.choice(word_list)
  word_length = len(chosen_word)
  
  end_of_game = False
  lives = 6
  
  
  print(logo)
  
  
  
  display = []
  for _ in range(word_length):
      display += "_"
  
  while not end_of_game:
      guess = input("Guess a letter: ").lower()
      clear()
      if guess in display:
        print(f"You already chose: '{guess}'")
  
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter
  
      if guess not in chosen_word:
          lives -= 1
          print(f"You lose a life, '{guess}' is not in the word!")
          if lives == 0:
              end_of_game = True
              print("You lose.")
  
  
      print(f"{' '.join(display)}")
  
  
      if "_" not in display:
          end_of_game = True
          print("You win.")
  
  
      print(stages[lives])

hangman()
run = input("Play Again Y/N  ").lower()
if run == "y":
    hangman()