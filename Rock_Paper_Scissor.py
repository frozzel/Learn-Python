def main():
  rock = '''
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  '''
  
  paper = '''
      _______
  ---'   ____)____
            ______)
            _______)
           _______)
  ---.__________)
  '''
  
  scissors = '''
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
  '''
  
  #Write your code below this line 👇
  
  import random
  
  print("********** Lets Play Rock, Paper, Scissors ************\n")
  ai = random.randint(0,2)
  image = [rock, paper, scissors]
  human = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
  if human < 0 or human >= 3:
    print("You Chose an invalid number, YOu lose!")
  else:
    print(image[human])
    print("Ai Chose:")
    print(image[ai])
    if human == 1 and ai == 0:
      print("You Win!")
    elif human == 2 and ai == 1:
      print("You Win!")  
    elif human == 0 and ai == 2:
      print("You Win!")
    elif human == ai:
     print("Its a tie!")
    else:
      print("AI Wins!")
  run = input("Play again? Y/N  ").lower()
  if run == "y":
    main()
  else:
    print("Goodbye!")
main()