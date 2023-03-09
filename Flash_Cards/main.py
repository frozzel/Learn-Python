from tkinter import *
import pandas
import random

# --------------------------- GLOBAL VAR SETUP ----------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT1 = ("Ariel", 80, "italic")
FONT2 = ("Ariel", 120, "bold")
current_card = {}
to_learn = {}

# ------------------------------ DATA SETUP ------------------------------- #
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    org_data = pandas.read_csv("./data/french_words.csv")
    to_learn = org_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# ----------------------------- FUNCTIONS -------------------------------- #
def flip_card():
    canvas.itemconfig(card_background, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)
    
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

##### Background Canvas #####
canvas = Canvas(width=800, height=526, )
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263,image=front_img)
card_title = canvas.create_text(400, 150,  font=FONT1, fill="black")
card_word = canvas.create_text(400, 263,  font=FONT2, fill="black")
canvas.config(bg=BACKGROUND_COLOR,  highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

##### Buttons #####
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(window, image=wrong_img, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, bd=0, command=next_card)
wrong_button.grid(row=2, column=0)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(window, image=right_img, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, bd=0, command=is_known)
right_button.grid(row=2, column=1)

#########################################################################

next_card()
window.mainloop()