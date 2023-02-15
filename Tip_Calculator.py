#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("******Welcome to the tip calculator!\n******")
bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
tip_percent = int(tip)/100
calc_tip = float(bill) * float(tip_percent)
total_with_tip = float(bill) + calc_tip
div_by_people = total_with_tip/int(people)
money = "{:.2f}".format(div_by_people)
# money = round(div_by_people, 2)
ans = f"Each person should pay: ${money}"

print(ans)