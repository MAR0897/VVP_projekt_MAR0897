import json
import importlib
import argparse
import planet
importlib.reload(planet)
from planet import Planet
import plotting as plot
importlib.reload(plot)
from numpy.linalg import norm

parser = argparse.ArgumentParser()
parser.add_argument("--input_file", type=str, required=True, help="path to JSON file with initial data")
parser.add_argument("--n", type=int, default=100, help="number of iterations")
parser.add_argument("--timestep", type=float, default=86400, help="time value in seconds (time passed after each iteration)")
parser.add_argument("--print_mode", type=int, default=1, help="printing mode: 0 - line plot, 1 - system plot (one body in the center), 2 - scatter plot, 3 - animation")
parser.add_argument("--random", type=int, default=0, help="randomized initial planet parameters")
parser.add_argument("--container", type=int, default=0, help="checks if the planets became degenerated")
args = parser.parse_args()

#Setting initial args
iter_n: int = args.n
print_mode: int = args.print_mode
dt: float = args.timestep
container: int = args.container
random = args.random
planets: list = []

#Reading from file, class initialization
with open(args.input_file, "r") as file:
    init_data: dict = json.load(file)
for name, data in init_data.items():
    if random == 0:
        planet = Planet(name, data["position"], data["velocity"], data["mass"], iter_n)
    else:
        planet = Planet.random(name, norm(data["position"]), norm(data["velocity"]), data["mass"], iter_n)
    planets.append(planet)

#Moving planets
degenerated = False
for i in range(iter_n):
    Planet.update_coords(Planet, planets, i, dt)
    if container==1 and i%100==0:
        for planet in planets:
            if Planet.is_too_far(planet):
                print("Simulation probably degenerated")
                degenerated = True
                break
        if degenerated:
            iter_n = i
            break

#Printing results
plot.plot(planets, print_mode, iter_n)
