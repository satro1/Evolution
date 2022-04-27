from World import *

width, height = 600, 500
n_creatures = 15
n_food = 50
initial_size = 5
initial_speed = 2
initial_color = "blue"


world = World(width, height, n_creatures, n_food, initial_size, initial_speed, initial_color)
world.run()