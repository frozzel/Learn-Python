import random#random module is imported

rando = random.randint(1,6)#random number between 1 and 6
print(rando)

rando_float = random.random()#random number between 0 and 1
print(rando_float)

combine = round((random.random() * 5), 2)#` * 5` to get a number between 0 and 5, `round()` to round to 2 decimal places
print(combine)