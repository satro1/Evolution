from world import *
import utils


params = utils.parse_json("parameters.json")
width, height = params["width"], params["height"]
n_creatures = params["n_creatures"]
n_food = params["n_food"]
initial_size = params["initial_size"]
initial_speed = params["initial_speed"]
initial_color = params["initial_color"]

world = World(width, height, n_creatures, n_food, initial_size, initial_speed, initial_color)
world.run()