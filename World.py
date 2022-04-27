from tkinter import *
from Balls import *

class World:
    def __init__(self, width, height, n_creatures, n_food, initial_size, initial_speed, initial_color):
        self.tk = Tk()
        self.width = width
        self.height = height
        self.canvas = Canvas(self.tk, width=width, height=height)
        self.canvas.pack()
        self.initialize_world(n_creatures, n_food, initial_size, initial_speed, initial_color)

    def initialize_world(self, n_creatures, n_food, initial_size, initial_speed, initial_color):
        self.creatures = [Creature(initial_size, initial_speed, initial_color,
                                   self.width, self.height, self.canvas, self.tk)
                          for _ in range(n_creatures)]
        self.food = [Food(self.width, self.height, self.canvas, self.tk)
                     for _ in range(n_food)]

    def run(self):
        for c in self.creatures:
            c.movement()
        for f in self.food:
            f.movement()
        self.tk.mainloop()