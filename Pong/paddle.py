from turtle import Turtle

MOVE_DIS = 20

class Paddle(Turtle):
    
    def __init__(self,position):
        super().__init__()
        self.create_paddle(position)
        
        
    def create_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)
        
    def up(self):
        new_y = self.ycor() + MOVE_DIS
        self.goto(self.xcor(), new_y)
        
        
    def down(self):
        new_y = self.ycor() - MOVE_DIS
        self.goto(self.xcor(), new_y)