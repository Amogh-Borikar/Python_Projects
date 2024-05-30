import tkinter as tk
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(numbers) for char in range(nr_symbols)]
    password_numbers = [random.choice(symbols) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    
    Password_input.delete(0, tk.END)
    Password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = Website_input.get()
    user = User_name_input.get()
    password = Password_input.get()
    
    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty fields not allowed!", 
                            message="Oops, you left some fields empty! Try again!")
    else:
        is_ok = messagebox.askokcancel(title=website, 
                            message=f"These are the details entered for {website}: \nEmail:"
                            f"{user}\nPassword: {password} \nIs it okay to save?")

        if is_ok:
            with open("Intermediate/D29_password_manager_tkinter/Data.txt", "a") as data_file:
                data_file.write(f"{website} | {user} | {password}\n")
                Website_input.delete(0, tk.END)
                Password_input.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=100, pady=70)

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
lock_image = tk.PhotoImage(file="Intermediate/D29_password_manager_tkinter/logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

Website_text = tk.Label(text="Website:")
Website_text.grid(column=0, row=1)

User_name_text = tk.Label(text="Email/User Name:")
User_name_text.grid(column=0, row=2)

Password_text = tk.Label(text="Password:")
Password_text.grid(column=0, row=3)

Website_input = tk.Entry(width=38)
Website_input.grid(column=1, row=1, columnspan=2)
Website_input.focus()

User_name_input = tk.Entry(width=38)
User_name_input.grid(column=1, row=2, columnspan=2)
User_name_input.insert(0, "xyz@xyz.com")

Password_input = tk.Entry(width=21)
Password_input.grid(column=1, row=3)

Generate_Button = tk.Button(text="Generate Password", command=password_generator)
Generate_Button.grid(column=2, row=3)

Add_Button = tk.Button(text="Add Password", width=36, command=save)
Add_Button.grid(column=1, row=4, columnspan=2)

window.mainloop()