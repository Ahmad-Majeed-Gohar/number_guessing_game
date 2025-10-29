import random
import tkinter as tk
from tkinter import messagebox

def check_guess():
    guess = int(entry.get())
    if guess == number:
        messagebox.showinfo("Result", "🎉 Correct! You guessed the number!")
        restart = messagebox.askyesno("Play Again", "Would you like to play again?")
        if restart:
            global number
            number = random.randint(1, 10)
    elif guess < number:
        messagebox.showinfo("Result", "Too low! Try again.")
    else:
        messagebox.showinfo("Result", "Too high! Try again.")

number = random.randint(1, 10)

root = tk.Tk()
root.title("Number Guessing Game")

tk.Label(root, text="Guess a number between 1 and 10").pack(pady=10)
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Submit", command=check_guess).pack(pady=10)

root.mainloop()