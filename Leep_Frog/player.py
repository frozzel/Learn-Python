from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 8
FINISH_LINE_Y = 280
MOVE_INCREASE = 2


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("purple")
        self.penup()
        self.setheading(90)
        self.play_speed = MOVE_DISTANCE
        self.go_to_start()
        
    def go_to_start(self):
        self.play_speed += MOVE_INCREASE
        self.goto(STARTING_POSITION)    
    
    def up(self):
        new_y = self.ycor() + self.play_speed
        self.goto(self.xcor(), new_y)
        
    def down(self):
        new_y = self.ycor() - self.play_speed
        self.goto(self.xcor(), new_y)
