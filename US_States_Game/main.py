import pandas
import turtle

screen = turtle.Screen()

screen.title("US States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_m(x,y):
#     print(x,y)
    
# turtle.onscreenclick(get_m)

# turtle.mainloop()


ans_state = screen.textinput(title="Guess A State", prompt="What's another state's name?").title()


screen.exitonclick()
