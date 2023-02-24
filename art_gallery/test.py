from turtle import Turtle, Screen

timmy = Turtle()
tommy = Turtle()

timmy.shape("turtle")
timmy.color("plum")
tommy.shape("turtle")
tommy.color("brown")
tommy.shapesize(2, 2)


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


def six_shapes(turtle):
    y = 3
    x = 3
    dis = 50
    angle = 360 / x
    while y < 11:
        x +=1
        dis +=50
        y += 1
        print(x, angle)
        for _  in range(x):
            turtle.fd(dis)
            turtle.left(angle)
      
        

# six_shapes(tommy)


def draw_shape(turtle, sides):
    angle = 360 / sides
    for _ in range(sides):
        turtle.fd(100)
        turtle.right(angle)
        
        
def turle_madness(turtle):
    for x in range(3,11):
        draw_shape(turtle, x)

turle_madness(timmy)
turle_madness(tommy)



screen = Screen()
screen.exitonclick()

