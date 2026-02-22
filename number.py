import tkinter as tk
import random


root = tk.Tk()
root.title("Guess the Number")
root.geometry("400x300")

secret = random.randint(1, 100)
def 

title_label = tk.Label(root, text="Guess the number!", font=("Arial", 18))

title_label.pack(pady=10)

prompt_label.pack
prompt_label = tk.Label(root, text="Enter a number (1-100)")

guess_entry = tk.Entry(root, width=10, justify="center")
guess_entry.pack(pady=5)

result_label = tk.Label(root, text="good luck!", font=("Arial", 14))
result_label.pack(pady=10)


root.mainloop()
