from turtle import Turtle, Screen
import random
import turtle as t
t.colormode(255)

timmy = Turtle()
# tommy = Turtle()

timmy.shape("turtle")
timmy.color("plum")
# tommy.shape("turtle")
# tommy.color("brown")
# tommy.shapesize(2, 2)


def draw_sq(turtle, dist, deg):
    for x in range(0,4):
        turtle.forward(dist)
        turtle.right(deg)
    
# draw_sq(tommy, 100, 90)
# draw_sq(timmy, 50, -90)

def draw_poop(turtle, dis):
    for x in range(dis):
        turtle.fd(5)
        turtle.up()
        turtle.fd(5)
        turtle.pd()

# draw_poop(timmy, 50)
# draw_poop(tommy, 25)

color = ["red", 'blue', 'green', 'purple', 'yellow', 'black', 'orange', ]


def draw_shape(turtle, sides):
    angle = 360 / sides
    for _ in range(sides):
        turtle.fd(100)
        turtle.right(angle)
        
        
def turle_madness(turtle):
    for x in range(3,11):
        turtle.color(random.choice(color))
        draw_shape(turtle, x)

# turle_madness(timmy)
# turle_madness(tommy)

left_right = [90, 0, 180, 270]

speed = [0,10,6,3,1]

def rando_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tuple = (r, g, b)
    return tuple

def rando_move(turtle):
    turtle.width(10)
    for _ in range(1, 50):
        turtle.speed(random.choice(speed))
        turtle.color(rando_color())
        turtle.fd(50)
        turtle.right( random.choice(left_right))

# rando_move(timmy)
# rando_move(tommy)

def draw_spirograph(size_gap):
    timmy.hideturtle()
    timmy.speed("fastest")
    for _  in range(int(360 / size_gap)):
        timmy.color(rando_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()

