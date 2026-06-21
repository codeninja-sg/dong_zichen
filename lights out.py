import tkinter as tk
import random

root = tk.Tk()
root.title('Lights Out')

grid = [
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
]
ROWS = 5
COLS = 5
grid = [[0]*COLS for _ in range(ROWS)]
grid = [[0] * COLS for _ in range(ROWS)]
buttons = []

for r in range(ROWS):
    for c in range(COLS):
        btn = tk.Button(root, width=6, height=3, bg='grey20')
        btn.grid(row=r, column=c, padx=2, pady=2)
        buttons.append(btn)

def toggle_cell(r, c):
    if 0 <= r < ROWS and 0 <= c < COLS:
        grid[r][c] = 1 - grid[r][c]
        if grid[r][c] == 1:
            colour = 'yellow'
        else:
            colour = 'grey20'
        buttons[r * COLS + c].config(bg=colour)

def on_click(r ,c):
    toggle_cell(r,    c)
    toggle_cell(r  -1,    c)
    toggle_cell(r  +1,    c)
    toggle_cell(r,    c -1)
    toggle_cell(r,    c +1)
    check_win()

root.mainloop()
