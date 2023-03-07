from tkinter import *

window = Tk()

window.title("Miles to Km Converter")
window.minsize(width=200, height=50)
window.config(padx=20, pady=20)

##### Functions ###########
def calculate():
    num = float(input.get())
    km = round(num * 1.609344)
    conv_label.config(text=km)




###########################
FONT = ("Arial", 14)


input = Entry(width=7)
input.insert(END, string=0)
input.grid(column=1, row=0)

mile_label = Label(text="Miles", font=FONT)
mile_label.grid(column=2, row=0)

label_equal = Label(text="is equal: ", font=FONT)
label_equal.grid(column=0, row=1)

conv_label = Label(text=0, font=FONT)
conv_label.grid(column=1, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

calc_button = Button(width=7, text="Calculate", command=calculate)
calc_button.grid(column=1, row=2)


window.mainloop()