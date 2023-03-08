from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate(): 
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    pass_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    pass_num = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = pass_letters + pass_symbols + pass_num
    random.shuffle(password_list)

    password = "".join(password_list)
    
    pass_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_file():
    website = website_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        website: {  
            "email": email,
            "password": password,
        }
    }
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
                website_input.delete(0, END)
                pass_input.delete(0, END)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
                website_input.delete(0, END)
                pass_input.delete(0, END)

# ---------------------------- SEARCH WEBSITES ------------------------------- #

def search():
    website = website_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            email = data[website]["email"]
            password = data[website]["password"]       
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Found. Please add a new entry.")
    except KeyError:
        messagebox.showwarning(title="Error", message=f"No details for {website.title()} exists.")
    else:
        messagebox.showwarning(title=f"{website.title()} Password", message=f"Your {website.title()} Credentials: \nPassword: {password}\nEmail: {email}")
    finally:
        website_input.delete(0, END)
        

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

website_input = Entry(width=21, bg='white', fg="black", highlightbackground="white")
website_input.grid(column=1, row=1,)
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
search_button = Button(text="Search", command=search,bg='white', fg="black", highlightbackground="white", width=10)
search_button.grid(column=2, row=1)

window.mainloop()