from tkinter import *
import random

def roll():
    # Generate two random numbers between 1 and 6
    r1 = random.randint(1, 6)
    r2 = random.randint(1, 6)
    s = f"{r1} and {r2}"  # Format the result to show both dice rolls
    e.delete(0, END)
    e.insert(0, s)

def on_enter(event):
    button1.config(fg="black")

def on_leave(event):
    button1.config(fg="green")

root = Tk()
root.geometry("150x150")  # Adjust window size to accommodate the changes
root.title("Dice")
label = Label(root, text="Simple Dice", wraplength=100)
e = Entry(root, width=10)  # Adjust width to accommodate two numbers
button1 = Button(root, text="Roll", command=roll, wraplength=100)

button1.bind("<Enter>", on_enter)
button1.bind("<Leave>", on_leave)

label.grid(row=0, sticky=N)
e.grid(row=2, sticky=N)
button1.grid(row=4, sticky=S)

root.mainloop()
