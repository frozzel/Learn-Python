#Data Types

#String

print("Hello"[4])# prints the 4th letter in the string "subscripting"

#integer

print(123 + 345)# prints the sum of the two numbers

#float

print(3.14159)# prints the float

#Boolean

True# prints True

False# prints False


#Type Error`
# print("Hello" + 5)# this will give a type error because you can't add a string and an integer`

type()# this will tell you the type of data type

#Type Conversion

str()# converts to a string

int()# converts to an integer

float()# converts to a float

bool()# converts to a boolean


#Example of Type Conversion

two_digit_number = input("Type a two digit number: ")# this will take the input and store it in the variable two_digit_number


a = two_digit_number[0] # this will take the first digit of the input and store it in the variable a

b = two_digit_number[1] # this will take the second digit of the input and store it in the variable b

result=int(a)+int(b)# this will add the two digits together and store it in the variable result

print(result)# this will print the result

#Mathematical Operations

# + addition

# - subtraction

# * multiplication

# / division (float)

# ** exponent

# // floor division (rounds down) integer division

# % modulo

#The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.

# PEMDAS

# () parenthesis

#f-strings
name = "John"
f"Hello {name}"# this will print Hello and the name variable like jquery

#Example of f-strings

score = 0

height = 1.8

isWinning = True

print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")# this will print your score is 0, your height is 1.8, you are winning is True