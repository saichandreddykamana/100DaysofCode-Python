from tkinter import *
import pandas as pd
import random
# -------------------------- CONSTANTS --------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
current_word_index = 0
# ---------------------------- Functionality ---------------------- #
try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/french_words.csv')
finally:
    data_dict = pd.DataFrame(data)
    data_dict = data_dict.to_dict(orient="records")


def get_random_word(action='wrong'):
    global current_word_index, flip_timer
    current_word_index = random.randint(0, len(data_dict)-1)
    window.after_cancel(flip_timer)
    random_wrd_dict = data_dict[current_word_index]
    canvas.itemconfig(word, text=random_wrd_dict['French'], fill="black")
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(card_img, image=card_front)
    flip_timer = window.after(3000, func=flip_card)
    if action == 'right':
        del data_dict[current_word_index]
        df = pd.DataFrame(data_dict, columns=["French", "English"])
        df.to_csv('data/words_to_learn.csv', index=False)


def flip_card():
    canvas.itemconfig(card_img, image=card_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=data_dict[current_word_index]['English'], fill="white")


# -------------------------- UI SETUP ---------------------------- #


window = Tk()
window.title("Flash Card Application")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

card_img = canvas.create_image(400, 263, image=card_front)
language = canvas.create_text(400, 150, text="French", font=("Calibri", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Calibri", 60, "bold"))
get_random_word()
canvas.grid(row=0, column=0, columnspan=2)


red_img = PhotoImage(file="images/wrong.png")
green_img = PhotoImage(file="images/right.png")

red_btn = Button(image=red_img, highlightthickness=0, borderwidth=0, command=lambda: get_random_word('wrong'))
red_btn.grid(row=1, column=0)
green_btn = Button(image=green_img, highlightthickness=0, borderwidth=0, command=lambda: get_random_word('right'))
green_btn.grid(row=1, column=1)

window.mainloop()
