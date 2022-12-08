import pandas
import tkinter
import random

BACKGROUND_COLOR = "#B1DDC6"
BACK_CARD_COLOR = "#92c3b1"
window = tkinter.Tk()
card = {}

def is_known():
    global data

    data.remove(card)
    new_english_list = [item["English"] for item in data]
    new_russian_list = [item["Russian"] for item in data]

    next_card()

    new_data = {"English": new_english_list, "Russian": new_russian_list}
    new_data_frame = pandas.DataFrame(new_data)
    new_data_frame.to_csv("data/actuality_word.csv", index=False)


def flip_card():
    canvas.itemconfig(canvas_background, image=image_back)
    language_label.config(text="Russian", bg=BACK_CARD_COLOR)
    word_label.config(text=card["Russian"], bg=BACK_CARD_COLOR)

def next_card():
    global card, flipp
    window.after_cancel(flipp)

    card = random.choice(data)
    english_word = card["English"]

    canvas.itemconfig(canvas_background, image=photo)
    language_label.config(text="English", bg='white')
    word_label.config(text=english_word, bg='white')

    flipp = window.after(3000, flip_card)

try:
    data = pandas.read_csv("data/actuality_word.csv")
except:
    data = pandas.read_csv("data/english_words.csv")

data = data.to_dict(orient='records')

window.config(bg=BACKGROUND_COLOR)
canvas = tkinter.Canvas(width=1000, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
photo = tkinter.PhotoImage(file="images/card_front.png")
image_back = tkinter.PhotoImage(file="images/card_back.png")
canvas_background = canvas.create_image(500, 300, image=photo)
canvas.grid(row=0, column=1, columnspan=3, rowspan=3)

flipp = window.after(3000, flip_card)

#Buttons
accept_image = tkinter.PhotoImage(file='images/right.png')
button_accept = tkinter.Button(image=accept_image, highlightthickness=0, command=is_known)
button_accept.grid(row=4, column=3, sticky='w')

wrong_image = tkinter.PhotoImage(file="images/wrong.png")
button_wrong = tkinter.Button(image=wrong_image, highlightthickness=0, command=next_card)
button_wrong.grid(row=4, column=1, sticky='e')

#Labels

language_label = tkinter.Label(text="Language", font=("Airal", 25, "normal"), bg="white", anchor='center')
language_label.grid(row=0, column=2, sticky='s')

word_label = tkinter.Label(text="Word", font=('Arial', 30, 'bold'), bg='white', anchor='center')
word_label.grid(row=1, column=2)

next_card()

window.mainloop()

