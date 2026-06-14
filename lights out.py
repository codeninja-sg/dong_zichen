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


