from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate(): 
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    pass_input.insert(END, string=password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_file():
    web = website_input.get()
    email = email_input.get()
    password = pass_input.get()
    if len(web) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered:\nEmail: {email} \nPassword: {password}\nIs it ok to save?")
        if is_ok:
                with open("data.txt", "a") as file:
                    file.write(f"{web} | {email} | {password} \n")
                website_input.delete(0, END)
                pass_input.delete(0, END)
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config( padx=50, pady=50, bg="white")

## Logo image ##

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

## Labels ##

website_label = Label(text="Website:", bg="white", fg="black")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg="white", fg="black")
email_label.grid(column=0, row=2)
pass_label = Label(text="Password:", bg="white", fg="black" )
pass_label.grid(column=0, row=3)

## Inputs ##

website_input = Entry(width=35, bg='white', fg="black", highlightbackground="white")
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
email_input = Entry(width=35, bg='white', fg="black", highlightbackground="white")
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(END, string="ballsUp@me.com")
pass_input = Entry(width=21, bg='white', fg="black", highlightbackground="white")
pass_input.grid(column=1, row=3, )

## Buttons ##

#Buttons

gen_pass_button = Button(text="Gen Password", command=generate,bg='white', fg="black", highlightbackground="white")
gen_pass_button.grid(column=2, row=3)
save_button = Button(text="Add", command=save_file,bg='white', fg="black", highlightbackground="white", width=33)
save_button.grid(column=1, row=4, columnspan=2)

window.mainloop()