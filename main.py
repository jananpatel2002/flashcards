from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
ARIAL_60_BOLD = ("Arial", 60, "bold")
ARIAL_40_ITALIC = ("Arial", 40, "italic")

# --------------------------------------- UI ---------------------------------------

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
canvas.create_image(450, 300, image=card_front)
canvas.grid(row=0, column=0, columnspan=2, padx=50)

# Buttons
right_button = Button(image=right_picture, highlightthickness=0)
wrong_button = Button(image=wrong_picture, highlightthickness=0)
right_button.grid(row=1, column=0, pady=20)
wrong_button.grid(row=1, column=1, pady=20)
window.mainloop()
