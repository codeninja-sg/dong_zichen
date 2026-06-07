import tkinter as tk
import random

root = tk.Tk()
root.title("Ball drop")

W = 400
H = 500

canvas = tk.Canvas(root, width=W, height=H, bg='black')
canvas.pack()

pad_w = 90
pad_h = 12
pad_x = W//2
pad_y = H - 40

paddle = canvas.create_rectangle(pad_x - pad_w//2, pad_y - pad_h//2, pad_x + pad_w//2, pad_y + pad_h//2, fill='cyan', outline='')

SPEED = 20

def move_left(event):
    global pad_x
    pad_x -= SPEED

    if pad_x < pad_w //2:
        pad_x = pad_w //2
    canvas.coords(paddle,pad_x - pad_w//2, pad_y - pad_h//2, pad_x + pad_w//2, pad_y + pad_h//2)

def move_right(event):
    global pad_x
    pad_x += SPEED

    if pad_x > W - pad_w //2:
        pad_x = W - pad_w //2
    canvas.coords(paddle,pad_x - pad_w//2, pad_y - pad_h//2, pad_x + pad_w//2, pad_y + pad_h//2)

ball_r = 12
ball_x = W // 2
ball_y = 100
ball_dx = 3
ball_dy = 3

ball = canvas.create_oval(ball_x - ball_r, ball_y - ball_r, ball_x + ball_r, ball_y + ball_r, fill='white', outline='')
score   = 0
game_over = False

score_label = tk.Label(root, text='Score: 0',font=('Arial', 14),bg = 'black', fg='white')

score_label.pack()

def game_loop():
    global ball_x, ball_y, ball_dx, ball_dy, ball_r, score, game_over

    if game_over:
        return
    
    ball_x += ball_dx
    ball_y += ball_dy

    if ball_x - ball_r <= 0 or ball_x + ball_r >= W:
        ball_dx = -ball_dx

    if ball_y - ball_r <= 0:
        ball_dy = -ball_dy

    pad_left  = pad_x - pad_w//2
    pad_right = pad_x + pad_w//2
    pad_top   = pad_y - pad_h//2

    if (ball_y + ball_r >= pad_top and ball_y + ball_r <= pad_top +10 and pad_left <= ball_x <= pad_right):
        ball_dy = -abs(ball_dy)
        score += 1
        score_label.config(text=f'Score: {score}')

    if ball_y + ball_r >= H:
        game_over = True
        canvas.create_text(W//2, H//2,
                           text= f'game over! Score: {score}',
                           font=('Arial',20, 'bold'), fill='red')
        return
    canvas.coords(ball, ball_x - ball_r, ball_y - ball_r, ball_x + ball_r, ball_y + ball_r)


    root.after(16, game_loop)
    

root.bind('<Left>',move_left)
root.bind('<Right>',move_right)



game_loop()
root.mainloop()
