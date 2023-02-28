from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet:", prompt="Which turtle will win the race: Enter Color:  ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
y_pos = [-125, -75, -25, 25, 75, 125]
turt_list = []


for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[index])
    turt_list.append(new_turtle)
        
        
if user_bet:
    is_race_on = True
    
while is_race_on:
     
    for turtle in turt_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
               print(f"You Won! The {winner} turtle is the winner!") 
            else:
                print(f"You've lost! The winner was {winner} turtle")
        ran_dist = random.randint(0, 10)
        turtle.forward(ran_dist)


screen.exitonclick()