import tkinter as tk
import random

root = tk.Tk()
root.title("snake - 1")

SIZE = 40
W = 800
H = 800

canvas = tk.Canvas(root, width=W, height=H, bg = "white")
canvas.pack()

snake = [(10, 10)]

dx = 1
dy = 0

food = (random.randint(0, W//SIZE - 1),random.randint(0, H//SIZE - 1))

def draw():
    canvas.delete("all")

    fx, fy = food
    canvas.create_rectangle(fx*SIZE, fy*SIZE, fx*SIZE+SIZE, fy*SIZE+SIZE,fill="red")

    for (x, y) in snake:
        canvas.create_rectangle(x*SIZE, y*SIZE, x*SIZE+SIZE, y*SIZE+SIZE,fill="blue")

draw()
root.mainloop()
        