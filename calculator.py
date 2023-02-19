# Calculator
from art import logo_calc

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide,}

def calculator():
  print(logo_calc)
  calculating = True
  
  n1 = float(input("Whats the first number?  "))
    
  for key in operations:
      print(key)
  while calculating:  
    op = input("Pick an operation: ")
    n2 = float(input("Whats the next number?  "))
    calc_func = operations[op]
    answer = calc_func(n1, n2)
    print(f"{n1} {op} {n2} = {answer}")
    run = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, 'e' to exit:  ").lower()
    if run == "y":
        n1 = answer
    elif run == "n":
      calculating = False
      calculator()
    else:
      calculating = False


calculator()