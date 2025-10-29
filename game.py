import random
import tkinter as tk
from tkinter import messagebox

# Initialize score
score = 0

def check_guess():
    global number, score
    try:
        guess = int(entry.get())
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a number!")
        return

    if guess == number:
        score += 1
        score_label.config(text=f"Score: {score}")
        messagebox.showinfo("Result", f"🎉 Correct! You guessed it!\nYour score is now {score}")
        restart = messagebox.askyesno("Play Again", "Would you like to play again?")
        if restart:
            number = random.randint(1, 10)
            entry.delete(0, tk.END)
        else:
            root.destroy()
    elif guess < number:
        messagebox.showinfo("Result", "Too low! Try again.")
    else:
        messagebox.showinfo("Result", "Too high! Try again.")

# Initialize random number
number = random.randint(1, 10)

root = tk.Tk()
root.title("Number Guessing Game")

# Score label
score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 12))
score_label.pack(pady=5)

# Game widgets
tk.Label(root, text="Guess a number between 1 and 10").pack(pady=10)
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Submit", command=check_guess).pack(pady=10)

root.mainloop()