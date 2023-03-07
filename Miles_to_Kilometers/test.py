import tkinter
from tkinter import *
window = tkinter.Tk()

window.title("GUI ME")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

def butt_click():
    word = input.get()
    label["text"] = word

#Label

label = tkinter.Label(text="Label Me", font=("Arial", 24, "bold"))
#Show label with pack call
# label.pack()
# label.place(x=100, y=200)
label.grid(column=0, row=0)
label.config(padx=10, pady=10)
#Buttons

button = tkinter.Button(text="Click Me", command=butt_click)
button2 = Button(text="Don't Click")
button.grid(column=1, row=1)
button2.grid(column=2, row=0)
# button.pack()

#Entry

input = Entry(width=10)
input.grid(column=3, row=2)
# input.pack()


# *args: Positional Variable-Length Arguments
def add(*args):
    # print(args[1])

    sum = 0
    for n in args:
        sum += n
    return sum
# print(add(3, 5, 6, 2, 1, 7, 4, 3))


# **kwargs: Keyworded Variable-Length Arguments
def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)

calculate(2, add=3, multiply=5)


# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline")
# print(my_car.model)

window.mainloop()