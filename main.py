import random
from tkinter import *
import pandas
import os

random_number = None
delayed_color_change = None
BACKGROUND_COLOR = "#B1DDC6"
ARIAL_60_BOLD = ("Ariel", 60, "bold")
ARIAL_40_ITALIC = ("Ariel", 40, "italic")
words_to_learn_list = []
# --------------------------------------- METHODS ---------------------------------------
try:
    if(os.path.getsize("./data/words_to_learn.csv")) < 3:
        raise FileNotFoundError
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    data_dict = pandas.DataFrame.to_dict(data, orient="records")  # Turns the whole csv file into a nice dictionary


def change_background(text):
    canvas.itemconfig(image, image=card_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=text, fill="white")


def generate_word():
    global delayed_color_change
    global random_number
    canvas.itemconfig(image, image=card_front)
    canvas.itemconfig(language, text="French", fill="black")
    random_number = random.randint(0, len(data_dict) - 1)
    canvas.itemconfig(word, text=data_dict[random_number]["French"], fill="black")
    delayed_color_change = window.after(3000, change_background, data_dict[random_number]["English"])


def right_clicked():
    window.after_cancel(
        delayed_color_change)  # Cancels the previous instance of the 3k millisecond timer incase user spams
    data_dict.remove({
        "French": data_dict[random_number]["French"],
        "English": data_dict[random_number]["English"]
    })
    df = pandas.DataFrame(data_dict)
    df.to_csv("./data/words_to_learn.csv", index=False)  # Makes a new csv file instantly after getting something right
    if len(data_dict) == 0:
        window.destroy()
        print(os.path.getsize("./data/words_to_learn.csv"))
    else:
        generate_word()


def wrong_clicked():
    window.after_cancel(delayed_color_change)
    generate_word()



# --------------------------------------- UI --------------------------------------------

window = Tk()
window.title("Flash Cards for France")
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
right_button = Button(image=right_picture, highlightthickness=0, command=right_clicked)
wrong_button = Button(image=wrong_picture, highlightthickness=0, command=wrong_clicked)
right_button.grid(row=1, column=0, pady=20)
wrong_button.grid(row=1, column=1, pady=20)

generate_word()
window.mainloop()
