# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

remaining_years = 90 - int(age)

days = 365 * remaining_years
weeks = 52 * remaining_years
months = 12 * remaining_years

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

