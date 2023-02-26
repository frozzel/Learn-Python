from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet:", prompt="Which turtle will win the race: Enter Color:  ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
turt_list = []

def start_line(colors):
    y= -125
    for color in colors:
        colors = Turtle(shape="turtle")
        colors.color(color)
        colors.penup()
        colors.goto(x=-230, y=y)
        y += 50
        

if user_bet:
    is_race_on =True
    
while is_race_on:
    
    ran_dist = random.randint(0, 10)
    colors.forward(ran_dist)

start_line(colors)
screen.exitonclick()