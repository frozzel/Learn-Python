print("Welcome to the rollercoaster!\n")
height = int(input("What is your height in cm? "))
if height > 120:
  print("You Can Ride!")
  age = int(input("Whats Your Age? "))
  if age < 12:
    print("The cost is $5")
  elif  age <=18:
    print("The cost is $7")
  else:
    print("The cost is $12")
else:
  print("You Can't Ride")