# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

to_lower = name1.lower() + name2.lower()
true_count = 0
true_count += to_lower.count("t")
true_count += to_lower.count("r")
true_count += to_lower.count("u")
true_count += to_lower.count("e")
love_count = 0
love_count += to_lower.count("l")
love_count += to_lower.count("o")
love_count += to_lower.count("v")
love_count += to_lower.count("e")
combine = str(true_count) + str(love_count)
total = int(combine)

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")