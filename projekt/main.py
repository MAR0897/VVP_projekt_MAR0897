import json
import importlib
from .planet import Planet
from .plotting import plot
from numpy.linalg import norm

class Simulace:
    def __init__(self, iter_n: int = 100, timestep: float = 86400, random: int = 0, container: int = 0) -> None:
        #Setting initial args
        self.iter_n = iter_n
        self.dt = timestep
        self.container = container
        self.random = random
        self.planets = []

    def read_from_file(self, input_file: str) -> None:
        #Reading from file, class initialization
        with open(input_file, "r") as file:
            init_data: dict = json.load(file)
        for name, data in init_data.items():
            if self.random == 0:
                planet = Planet(name, data["position"], data["velocity"], data["mass"], self.iter_n)
            else:
                planet = Planet.random(name, norm(data["position"]), norm(data["velocity"]), data["mass"], self.iter_n)
            self.planets.append(planet)

    def simulate(self) -> None:
        #Moving planets
        degenerated = False
        for i in range(self.iter_n):
            Planet.update_coords(Planet, self.planets, i, self.dt)
            if self.container==1:
                for planet in self.planets:
                    if Planet.is_too_far(planet):
                        print("Simulation probably degenerated")
                        degenerated = True
                        break
                if degenerated:
                    self.iter_n = i
                    break

    def print(self, print_mode: int = 0) -> None:
        plot(self.planets, print_mode, self.iter_n)
