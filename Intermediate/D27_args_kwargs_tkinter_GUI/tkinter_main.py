import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=1000, height=700)
window.config(padx=20, pady=20)

def button_clicked():
    print("I got clicked")
    my_label.config(text=f"you typed {input.get()}")

my_label = tkinter.Label(text="This is label", font=("Ariel", 50, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=30)

my_button = tkinter.Button(text="click me", command=button_clicked)
my_button.grid(column=0, row=1)

input = tkinter.Entry(width=20)
input.grid(column=2, row=2)

new_button = tkinter.Button(text="this is a new button", command=button_clicked)
new_button.grid(column=3, row=3)

window.mainloop()

