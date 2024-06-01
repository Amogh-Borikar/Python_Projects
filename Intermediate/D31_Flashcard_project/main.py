from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("Intermediate/D31_Flashcard_project/data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)

window = Tk()
window.title("Amogh's Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)

card_front = PhotoImage(file="Intermediate/D31_Flashcard_project/images/card_front.png")
card_back = PhotoImage(file="Intermediate/D31_Flashcard_project/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)

card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


cross = PhotoImage(file="Intermediate/D31_Flashcard_project/images/wrong.png")
cross_button = Button(image=cross, highlightthickness=0, command=next_card)
cross_button.grid(column=0, row=1)

right = PhotoImage(file="Intermediate/D31_Flashcard_project/images/right.png")
right_button = Button(image=right, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
