############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20): change to 21
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)    change 1 to 0 because index starts at 0 and change 6 to 5
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994: added >=
#   print("You are a Gen Z.")
# else:
#   print("Boomer") added else for prior years

# # Fix the Errors
# age = input("How old are you?") age needs to be int
# if age > 18:
# print("You can drive at age {age}.") need to indent for if statement and add 'f' to use age

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) should be = not ==
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item) inproper indent 
#   print(b_list)

# mutate([1,2,3,5,8,13])