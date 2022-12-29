import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
ARIAL_60_BOLD = ("Ariel", 60, "bold")
ARIAL_40_ITALIC = ("Ariel", 40, "italic")
# --------------------------------------- METHODS ---------------------------------------


data = pandas.read_csv("./data/french_words.csv")
data_dict = pandas.DataFrame.to_dict(data, orient="records")  # Turns the whole csv file into a nice dictionary


def change_background(text):
    canvas.itemconfig(image, image=card_back)
    canvas.itemconfig(language,text="English",fill="white")
    canvas.itemconfig(word, text=text,fill="white")


def generate_word():
    random_number = random.randint(0, len(data_dict))
    canvas.itemconfig(word, text=data_dict[random_number]["French"])
    delayed_color_change = window.after(3000, change_background, data_dict[random_number]["English"])



# --------------------------------------- UI --------------------------------------------

window = Tk()
window.config(bg=BACKGROUND_COLOR)
window.minsize(width=900, height=800)
canvas = Canvas(width=850, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)

# Photo Images
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right_picture = PhotoImage(file="./images/right.png")
wrong_picture = PhotoImage(file="./images/wrong.png")

# Canvas
image = canvas.create_image(450, 300, image=card_front)
canvas.grid(row=0, column=0, columnspan=2, padx=50)
language = canvas.create_text(450, 150, text="French", font=ARIAL_40_ITALIC)
word = canvas.create_text(450, 300, text="Word", font=ARIAL_60_BOLD)

# Buttons
right_button = Button(image=right_picture, highlightthickness=0, command=generate_word)
wrong_button = Button(image=wrong_picture, highlightthickness=0, command=generate_word)
right_button.grid(row=1, column=0, pady=20)
wrong_button.grid(row=1, column=1, pady=20)
window.mainloop()
