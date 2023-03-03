import time
from turtle import Screen
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
cars = CarManager()
score = Scoreboard()


screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.create_car2()
    cars.move_cars()
    cars.move_cars2()
    ## resest player position
    if player.ycor() > 280:
        player.go_to_start()
        score.update_scoreboard()
        cars.level_up()
        
    ## detect collision with car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
            
    for car in cars.top_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

         
screen.exitonclick()
        