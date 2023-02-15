print("Welcome to the rollercoaster!\n")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
  print("You Can Ride!")
  age = int(input("Whats Your Age? "))
  if age < 12:
    bill = 5
    print("The child ticket cost is $5")
  elif  age <=18:
    bill = 7
    print("The teen ticket cost is $7")
  elif age >= 45 and age <= 55:
    print("Everything is going to be okay. Have a free ride on us!")
  else:
    bill = 12
    print("The adult ticket cost is $12")

  photo = input("Do you want a photo taken? Y or N. ")
  if photo == "Y":
    bill += 3
  print(f"Your final bill is ${bill}")

else:
  print("You Can't Ride")