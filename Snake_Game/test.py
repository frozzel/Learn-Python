from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from scoreboard import Score
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
snack = Food()
score = Score()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
 
snake_go = True
while snake_go:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    
    if snake.head.distance(snack) < 15:
        snack.refresh()
        snake.extend()
        score.increase_score()
        
    if snake.head.xcor() > 280  or snake.head.xcor() < -280 or snake.head.ycor() > 280  or snake.head.ycor() < -280:
        snake_go = False 
        score.game_over() 
        
    for seg in snake.snake_list[1:]:
        if snake.head.distance(seg) < 10:
            snake_go = False 
            score.game_over()
            


screen.exitonclick()
