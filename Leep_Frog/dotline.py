from turtle import Turtle

class Dot_Line(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=.6, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)
        self.draw_line()
        
        
    def draw_line(self):
        for _ in range(10):   
            self.stamp()
            self.penup()
            self.fd(60)
            self.pendown()
      