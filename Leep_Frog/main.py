import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from grass import Grass
from dotline import Dot_Line

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray")
screen.title("Turtle Crossing")
screen.tracer(0)

grass = Grass((0, -290), "green", 1)
grass2 = Grass((0, 300), "green", 1)
yellow = Grass((0, -4), "yellow", .1)
yellow2 = Grass((0, 4), "yellow", .1)
line1 = Dot_Line((-280, -150))
line2 = Dot_Line((-280, 150))
player = Player()


screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    