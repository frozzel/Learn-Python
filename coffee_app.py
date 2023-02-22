#import data
from data import resources, MENU
from replit import clear

#function to check resources
def fill_coffee():
    resources['water'] += 300
    resources['milk'] += 200
    resources['coffee'] += 100
    resources['Money'] -= 2
    

def make_coffee(bev_choice):
    choice = MENU[bev_choice]["ingredients"]
    if choice['water'] > resources['water'] or choice['milk'] > resources['milk'] or choice['coffee'] > resources['coffee']:
        return False
    else:
        resources['water'] = resources['water'] - choice['water']
        resources['milk'] = resources['milk'] - choice['milk']
        resources['coffee'] =resources['coffee'] - choice['coffee']
        resources['Money'] = resources['Money'] + MENU[bev_choice]["cost"]
        return True
    
    
def compare(money, choice):
    cost = MENU[choice]["cost"]
    if cost > money:
        return("Sorry that's not enough money. Money refunded.")
    else:
        return money - cost
    
    
def coin():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))* .25
    dimes = int(input("how many dimes?: "))* .10
    nickles = int(input("how many nickles?: "))* .05
    pennies = int(input("how many pennies?: "))* .01
    money = quarters + dimes + nickles + pennies
    return money

def choice(bev_choice):
    if bev_choice == 'report':
        print(f'Water:  {resources["water"]}ml\nMilk:   {resources["milk"]}ml\nCoffee:  {resources["coffee"]}g\nMoney:  ${resources["Money"]}')
    elif bev_choice == 'fill':
        fill_coffee()
    elif bev_choice == 'latte'or bev_choice == 'espresso'or bev_choice == 'cappuccino':
        money = coin()
        change = compare(money, bev_choice)
        if change == "Sorry that's not enough money. Money refunded.":
            print(change)
        else:
            inventor = make_coffee(bev_choice)
            if inventor:
                change = round(change, 2)
                print(f"Here is {change} in change.")
                print(f"Here is your {bev_choice} ☕. Enjoy!")
            else:
                print("Theres not enough resources")
                
                
                   
                   

#globals


brew = True

print("☕ Welcome to the Coffee Machine ☕")
while brew:
    bev_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if bev_choice == "off":
        brew =False
    choice(bev_choice)

