from turtle import Turtle

class Grass(Turtle):
    def __init__(self, position, color, width):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=width, stretch_len=30)
        self.color(color)
        self.penup()
        self.goto(position)