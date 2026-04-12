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
        canvas.create_rectangle(x*SIZE, y*SIZE, x*SIZE+SIZE, y*SIZE+SIZE,fill="green")


def game_loop():
    global snake, food
    
    head_x, head_y = snake[0]

    max_x = W // SIZE
    max_y = H // SIZE
    new_head = (head_x + dx, head_y + dy)

    if new_head[0] < 0 or new_head[0] >= max_x or new_head[1] < 0 or new_head[1] >= max_y:
        game_over = True
        print("hit")
        #status_label.config(text="game over: Hit the wall!")
        return
    if new_head in snake:
        game_over = True
        print("bite")
        return
    

   

    snake.insert(0, new_head)
    if new_head == food:

        food = (random.randint(0, W//SIZE - 1),random.randint(0, H//SIZE - 1))

    else:
        snake.pop()

    draw()
    root.after(150, game_loop)

   

def up(event):
    global dx, dy
    dx, dy = 0, -1

def down(event):
    global dx, dy
    dx, dy = 0, 1

def left(event):
    global dx, dy
    dx, dy = -1, 0

def right(event):
    global dx, dy
    dx, dy = 1, 0

root.bind("<Up>", up)
root.bind("<Down>", down)
root.bind("<Left>", left)
root.bind("<Right>", right)

game_over = False
if game_over:
    print("game over!")

def restart():
    global snake, dx, dy, food, game_over
    snake = [(10, 10)]
    dx, dy = 1, 0
    food = (random.randint(0, W//SIZE - 1),random.randint(0, H//SIZE - 1))

    game_over = False
    #status_label.config(text="")
    draw()
    root.after(150, game_loop)

restart_btn = tk.Button(root, text="Restart",command=restart)
restart_btn.pack(pady=5)


draw() 
root.after(150, game_loop)
root.mainloop()
        
