from tkinter import *
from Creature import *
import numpy as np

width, height = 600, 500
tk = Tk()
canvas = Canvas(tk, width=width, height=height)
canvas.pack()

n = 15
colors = ['red', 'green', 'blue', 'yellow', 'white']
for _ in range(n):
    size = ((-1)**np.random.randint(0,2)) * (np.random.rand()*20 + 5)
    speed = ((-1)**np.random.randint(0,2)) * (np.random.rand()*13 + 2)
    creature = Creature(size, speed, colors[np.random.randint(0, 5)], width, height, canvas, tk)
    creature.movement()

tk.mainloop()