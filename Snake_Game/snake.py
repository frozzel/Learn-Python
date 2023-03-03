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
            self.add_seg(index)
            
    def add_seg(self, index):
        n_snake = Turtle(shape= "square")
        n_snake.color("green")
        n_snake.penup()
        n_snake.goto(index)
        self.snake_list.append(n_snake)
        
        
    def extend(self):
        self.add_seg(self.snake_list[-1].position())
            
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
            
    def reset_snake(self):
        for seg in self.snake_list:
            seg.goto(1000, 1000)
        self.snake_list.clear()
        self.create_snake()
        self.head = self.snake_list[0]