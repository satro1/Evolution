from tkinter import *
from Balls import *
import numpy as np

width, height = 600, 500
n_creatures = 15
n_food = 50
initial_size = 5
initial_speed = 2
initial_color = "blue"

tk = Tk()
canvas = Canvas(tk, width=width, height=height)
canvas.pack()

for _ in range(n_creatures):
    creature = Creature(initial_size, initial_speed, initial_color, width, height, canvas, tk)
    creature.movement()

for _ in range(n_food):
    food = Food(width, height, canvas, tk)


tk.mainloop()