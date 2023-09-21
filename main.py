from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(400, 200)
window.config(padx=50, pady=50)

FONT = ("Arial", 15, "normal")
is_equal_to_label = Label(text="is equal to", font=FONT)
is_equal_to_label.grid(row=1, column=0)
entry = Entry(width=15)
entry.grid(row=0, column=1)
entry.insert(END, string="0")


def calculate():
    miles = int(entry.get())
    new_ans = miles * 1.60934
    answer_label["text"] = round(new_ans, 1)


miles_label = Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=2)
answer_label = Label(text=0, font=FONT)
answer_label.grid(row=1, column=1)
kilometer_label = Label(text="Km", font=FONT)
kilometer_label.grid(row=1, column=2)
button = Button(text="Calculate", font=FONT, command=calculate)
button.grid(row=2, column=1)

window.mainloop()
