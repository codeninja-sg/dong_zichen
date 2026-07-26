import tkinter as tk
import random

root = tk.Tk()
root.title("pong")

W = 600
H = 400

canvas = tk.Canvas(root, width=W, height=H, bg='black')
canvas.pack()

for y in range(0, H, 20):
    canvas.create_rectangle(W//2 - 2, y, W//2 + 2, y + 10, fill='grey30', outline='')

PAD_W = 12
PAD_H = 70
PAD_OFF = 20

p1_y = H // 2
p1 = canvas.create_rectangle(PAD_OFF,   p1_y - PAD_H//2,PAD_OFF + PAD_W,   p1_y + PAD_H//2,fill='cyan', outline='')

p2_y = H // 2
p2 = canvas.create_rectangle(W - PAD_OFF - PAD_W,  p2_y - PAD_H//2,W - PAD_OFF,   p2_y + PAD_H//2,fill='orange', outline='')

BALL_R = 8
ball_x = W // 2
ball_y = H // 2
ball_dx = random.choice([-4, 4])
ball_dy = random.choice([-3, 3])

root.mainloop()
