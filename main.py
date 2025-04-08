import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
from pathfinding import astar
from visualization import visualize

def start_app():
    try:
        rows = int(row_entry.get())
        cols = int(col_entry.get())
        density = float(obstacle_entry.get())
        if not (0 <= density <= 1):
            raise ValueError
    except:
        messagebox.showerror("Invalid Input", "Please enter valid numbers!\nObstacle Density must be between 0 and 1.")
        return

    status_label.config(text="Searching Path...", foreground="#FFD700")
    root.update_idletasks()

    grid = [[0 if random.random() > density else 1 for _ in range(cols)] for _ in range(rows)]

    start = (0, 0)
    end = (rows - 1, cols - 1)
    grid[start[0]][start[1]] = 0
    grid[end[0]][end[1]] = 0

    path = astar(grid, start, end)
    if not path:
        messagebox.showinfo("Result", "No path found!")
    visualize(grid, start, end, path)
    status_label.config(text="Ready", foreground="#00FF00")

def on_enter(e):
    e.widget['background'] = '#444'
    e.widget['foreground'] = '#FFD700'

def on_leave(e):
    e.widget['background'] = '#222'
    e.widget['foreground'] = 'white'

root = tk.Tk()
root.title("Mouse AI Pathfinder")

root.geometry("500x400")
root.resizable(False, False)

# Load Background Image
bg_img = Image.open("assets/background.jpg")
bg_img = bg_img.resize((500, 400), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_img)

canvas = tk.Canvas(root, width=500, height=400)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

frame = tk.Frame(root, bg="#000000", bd=2)
frame.place(relx=0.5, rely=0.45, anchor="center")

title = tk.Label(frame, text="Mouse AI Pathfinder", font=("Comic Sans MS", 18, "bold"), fg="#00FFFF", bg="#000000")
title.grid(row=0, column=0, columnspan=2, pady=10)

labels = ["Number of Rows:", "Number of Columns:", "Obstacle Density (0-1):"]
entries = []

for i, text in enumerate(labels, start=1):
    tk.Label(frame, text=text, font=("Arial", 12), fg="white", bg="#000000").grid(row=i, column=0, sticky="e", padx=8, pady=5)
    entry = tk.Entry(frame, width=15, font=("Arial", 12))
    entry.grid(row=i, column=1, pady=5)
    entries.append(entry)

row_entry, col_entry, obstacle_entry = entries

start_btn = tk.Button(frame, text="Start Pathfinding", command=start_app, font=("Arial", 13, "bold"),
                      bg="#222", fg="white", activebackground="#555", activeforeground="#FFD700", padx=8, pady=4)
start_btn.grid(row=4, column=0, columnspan=2, pady=15)

start_btn.bind("<Enter>", on_enter)
start_btn.bind("<Leave>", on_leave)

# Status Bar
status_label = tk.Label(root, text="Ready", font=("Arial", 11, "italic"), bg="#000000", fg="#00FF00", anchor="w")
status_label.place(relx=0, rely=1, relwidth=1, anchor="sw")

root.mainloop()
