import tkinter as tk
root = tk.Tk
root.title("Drawing pad")
root.geometry("800x600") # optional

controls = tk.frame(root)
controls.grid(row=0, column=0, stiky="ew", padx=8, pady=8)

canvas = tk.canvas(root, bg="white", width=760, hieght=480)
controls.grid(row=0, column=0, stiky="nsew", padx=8, pady=8)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)




root.mainloop()