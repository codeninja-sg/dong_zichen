import tkinter as tk
root = tk.Tk()
root.title("buttons & display")

title_lable = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 18))
title_lable.pack(pady=10)

name_label = tk.Label(root, text="your name:")
name_label.pack()

name_entry = tk.Entry(root, text="your name:")
name_entry.pack(pady=5)

def say_hello():
    name = name_entry.get().strip()
    if name:
        title_lable.config(text=f"Hello, {name}!")
    else:
        title_lable.config(text="Hello, Tkinter!")
hello_btn = tk.Button(root, text="say hello", command=say_hello)
hello_btn.pack(pady=5)

root.mainloop()
