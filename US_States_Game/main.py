import pandas
import turtle
from state import State

screen = turtle.Screen()

screen.title("US States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")

## get cordinates manualy for data
# def get_m(x,y):
#     print(x,y)
# turtle.onscreenclick(get_m)
# turtle.mainloop()
g_states = []
test_list = data.state.to_list()
states_list = test_list

while len(g_states) < 50:
    ans_state = screen.textinput(title=f"{len(g_states)}/50 States Correct", prompt="What's another state's name?").title()
    if ans_state == "Exit":
        break
        
    for name in data.state:
        if name == ans_state:
            g_states.append(ans_state)
            states_list.remove(ans_state)
            current_state = data[data.state == f'{name}']
            x = current_state.x.item()
            y = current_state.y.item()
            new_state = name
            new_state = State()
            new_state.create_state(name, x, y)
          
# print(states_list)
with open("states_to_learn.csv", mode="w") as file:
    for state in states_list:
        file.write(f"{state}\n")