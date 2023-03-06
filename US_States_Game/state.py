from turtle import Turtle

class State(Turtle):
    def __init__(self):
        super().__init__()
        
        
    def create_state(self, name, x, y):
        self.shape("circle")
        self.shapesize(.2)
        self.penup()
        self.goto(x, y)
        self.write(f"{name}")