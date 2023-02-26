from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_fw():
    tim.forward(10)
    
def move_back():
    tim.forward(-10)
    
def move_couter():
    tim.right(-25)
    
    
def move_clock():
    tim.right(25)
   
    
def clear_reset():
    tim.clear()
    tim.reset()

screen.listen()
screen.onkey(key="w", fun=move_fw)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=move_couter)
screen.onkey(key="d", fun=move_clock)
screen.onkey(key="c", fun=clear_reset)

screen.exitonclick()