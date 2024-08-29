from tkinter import *
from tkinter import messagebox
import random as r
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    n =r.randint(8,10)
    symbols = r.randint(2,4)
    numbers = r.randint(2,4)
    Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ,"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] 
    symbolsTable = ["!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~"]
    numbersTable = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    password = []
    password_letters =[r.choice(Alphabet) for i in range(n)]
    password_symbols = [r.choice(symbolsTable) for i in range(symbols)]
    password_numbers = [r.choice(numbersTable) for i in range(numbers)]
    password_list = password_letters + password_symbols + password_numbers
    r.shuffle(password_list)
    password = "".join(password_list)
    input_pass.delete(0, END)
    input_pass.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_data():
    new_data = {
        input_web.get(): {
            "email": input_user.get(),
            "password": input_pass.get()
        }
    }
    if len(input_web.get()) == 0 or  len(input_pass.get()) == 0:
            messagebox.showerror(title="Error", message="Please don't leave any field empty !")

    else:
        rep = messagebox.askokcancel(title="Data", message=f"Are you sure your website is {input_web.get()}, email is {input_user.get()} and password is {input_pass.get()}, please confirm ?")
        if rep : 
            try:
                with open ("data.json", mode="r") as file:
                    data =json.load(file)
            except FileNotFoundError:
                with open ("data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open ("data.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                input_web.delete(0, END)
                input_pass.delete(0, END)
def seach_data():
    try:
        with open ("data.json", mode="r") as file:
            data =json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if input_web.get() in data:
            email =data[input_web.get()]["email"]
            password =data[input_web.get()]["password"]
            messagebox.showinfo(title=f"{input_web.get()}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message="No details for the website exists")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1 ) 

web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

input_web = Entry(width=35)
input_web.grid(row=1, column=1, columnspan=2)

user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)

input_user = Entry(width=35)
input_user.insert(0, "amadou@gmail.com")
input_user.grid(row=2, column=1, columnspan=2)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

input_pass = Entry(width=21)
input_pass.grid(row=3, column=1)

generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(row=3, column=2)

seach_button = Button(text="Search", width=14, command=seach_data)
seach_button.grid(row=1, column=3)


add = Button(text="Add", width=36, command=add_data)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()





