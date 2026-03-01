import tkinter as tk
import random


root = tk.Tk()

root.title("Guess the Number")
root.geometry("400x300")

secret = random.randint(1, 100)
def check_guess():
    text = guess_entry.get().strip()

    if not text.isdigit():
        result_label.config(text="pls enter a number!")
        return
    
    guess =  int(text)

    if guess < secret:
        result_label.config(text="too low!")
    elif guess > secret:
        result_label.config(text="too high!")
    else:
        result_label.config(text=f"you got it! The number is {secret}.")

check_btn =tk.Button(root, text="check", command=check_guess)
check_btn.pack(pady=5)

def reset_game():
    global secret
    secret = random.randint(1, 100)
    result_label.config(text="New game! Guess again.")
    guess_entry.delete(0, tk.END)

reset_btn = tk.Button(root, text="reset", command=reset_game)
reset_btn.pack(pady=5)
