import tkinter.messagebox
from tkinter import *
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import messagebox


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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

    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    if website_data != "" and email_data != "" and password_data != "":
        permission = messagebox.askokcancel(title=website_data, message=f"{email_data} is email correct? \n {password_data} is password correct? \n Is it okay to save?")
        if permission:
            entry_data = f"{website_data} | {email_data} | {password_data}\n"
            with open('data.txt', 'a') as file:
                file.write(entry_data)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
    else:
        messagebox.showerror(title="Empty Fields", message="One or more fields are empty")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Mananger")
window.config(bg="white", padx=50, pady=50)


canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(width=15, text="Website", font=("Calibri", 11, "bold"), background="white")
website_label.grid(row=1, column=0)

email_label = Label(width=15, text="Email/Username", font=("Calibri", 11, "bold"), background="white")
email_label.grid(row=2, column=0)

password_label = Label(width=15, text="Password", font=("Calibri", 11, "bold"), background="white")
password_label.grid(row=3, column=0)

website_entry = Entry(width=50, font=("Calibri", 11, "bold"))
website_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
website_entry.config(border="2px solid black", borderwidth=2)
website_entry.focus()

email_entry = Entry(width=50, font=("Calibri", 11, "bold"))
email_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
email_entry.config(border="2px solid black", borderwidth=2)
email_entry.insert(0, 'sai9318@gmail.com')

password_entry = Entry(width=34, font=("Calibri", 11, "bold"))
password_entry.grid(row=3, column=1, padx=5, pady=5)
password_entry.config(border="2px solid black", borderwidth=2)

generate_password_button = Button(text="Generate Password")
generate_password_button.config(background="#5897EE", foreground="white", command=password_generator)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="ADD", width=36)
add_button.grid(row=4, column=1, columnspan=2, pady=20)
add_button.config(background="#5897EE", foreground="white", command=save_data)
window.mainloop()
