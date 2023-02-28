from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    
    
    def  __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]
     
    def create_snake(self):
        for index in POSITIONS:
            n_snake = Turtle(shape= "square")
            n_snake.color("white")
            n_snake.penup()
            n_snake.goto(index)
            self.snake_list.append(n_snake)
            
    def snake_move(self):
        for snake in range( len(self.snake_list)-1, 0, -1):
            new_x = self.snake_list[snake - 1].xcor()
            new_y = self.snake_list[snake - 1].ycor()
            self.snake_list[snake].goto(new_x, new_y)
        self.head.fd(MOVE_DIS)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)