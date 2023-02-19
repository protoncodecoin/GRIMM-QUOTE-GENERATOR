from tkinter import *
import random
from quotes import all_seasons

FONT = ("Arial", 15, "bold")


def raw_quote_formatter():
    new_quote = all_seasons.split("\n")
    ran_quote = random.choice(new_quote)

    if len(ran_quote) > 2:
        formatted_line = ran_quote.split("|")
        episode = formatted_line[0]
        title = formatted_line[1]
        quote = formatted_line[2]
        source = formatted_line[3]

        canvas.itemconfig(quote_text, text=quote)
        canvas.itemconfig(episode_text, text=f"Episode:\n {episode}")
        canvas.itemconfig(source_text, text=f"Source:\n{source}")
        canvas.itemconfig(title_text, text=f"Title:\n{title}")
        # new_bg_image = PhotoImage(file=f"images/grimm_{random.randrange(1, 15)}.png")
        # canvas.itemconfig(image, image=new_bg_image)



window = Tk()
window.title("GRIMM QUOTES")
window.config(pady=5, padx=5, bg="Black")

# canvas
image_index = random.randrange(1, 15)
print(image_index)
background_image = PhotoImage(file=f"images/grimm_{image_index}.png")
canvas = Canvas(width=800, height=600, bg="black", highlightthickness=0)
image = canvas.create_image(400, 400, image=background_image)
quote_text = canvas.create_text(400, 320, text="",
                                fill="yellow",
                                width=350, font=FONT)
episode_text = canvas.create_text(195, 550, width=200, text="", fill="yellow", font=FONT)
source_text = canvas.create_text(600, 550, text="", width=200, fill="yellow", font=FONT)
title_text = canvas.create_text(400, 170, text="", fill="yellow", width=200, font=FONT)
canvas.grid(row=1, column=1, columnspan=2)

button = Button(text="GRIMM", bg="yellow", command=raw_quote_formatter)
button.grid(row=2, column=1, columnspan=2)
button.config(padx=20, pady=10, font=FONT)

raw_quote_formatter()

window.mainloop()
