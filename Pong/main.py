from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
ball = Ball()
score = Score()


screen.listen()
screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")
screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #Detect collision with paddle
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    if ball.xcor() > 380:
        ball.reset_position()
        score.r_point()
        score.update_score()
        
    if  ball.xcor() < -380:
        ball.reset_position()
        score.l_point()
        score.update_score()
        
    #Detect winner
    if score.score_count_pd1 == 5 or score.score_count_pd2 == 5:
        game_on = False
        score.game_over()

screen.exitonclick()