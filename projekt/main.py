"""
Module with class Simulation
"""
import json
import importlib
from . import planet
importlib.reload(planet)
from .planet import Planet
from numpy.linalg import norm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy import linspace

CMAPS = ["Blues", "Reds", "Greens", "Purples", "Oranges", "Greys"]
COLORS = ["orangered", "gray", "goldenrod", "lime", "indianred", "peru", "khaki", "aqua", "royalblue"]

class Simulation:
    """
    A class, whose instance represents one simulation.
    Variables:
        iter_n: int
        dt: float
        planets: list
    Methods:
        __init__(self, iter_n: int = 100, timestep: float = 86400) -> None:
        read_from_file(self, input_file: str, random: bool = False) -> None:
        simulate(self, container: bool = False) -> None:
        plot_image(self, print_mode: int) -> None:
        plot_video(self, output_file: str = "animation.gif") -> None:
    """

    def __init__(self, iter_n: int = 100, timestep: float = 86400) -> None:
        """__init__(self, iter_n: int = 100, timestep: float = 86400) -> None:
        Initializes basic simulation values - iter_n (number of iterations), dt (timestep), sim_n (number of finished simulations) -
        and creates a list of the simulation planets.
            sim_n = 0; number of finished simulations
        """
        self.iter_n = iter_n
        self.dt = timestep
        self.planets: list = []

    def read_from_file(self, input_file: str, random: bool = False) -> None:
        """read_from_file(self, input_file: str, random: bool = False) -> None:
        Reads initial parameters from a JSON file, initializes instances of class Planet and appends each planet to a list of planets.
        """
        with open(input_file, "r") as file:
            init_data: dict = json.load(file)
        for name, data in init_data.items():
            planet = Planet(name, data["position"], data["velocity"], data["mass"], self.iter_n, random)
            self.planets.append(planet)

    def simulate(self, container: bool = False) -> None:
        """simulate(self, container: bool = False) -> None:
        Simulates the planet movement, with given number of iterations and parameters from the input file. If parameter container is set to True, checks also
        if the simulation degenerated, and if yes, ends the simulation.
        """
        degenerated = False
        for i in range(self.iter_n):
            Planet.update_coords(Planet, self.planets, i, self.dt)
            if container:
                for planet in self.planets:
                    if Planet.is_too_far(planet):
                        print("Simulation probably degenerated")
                        degenerated = True
                        break
                if degenerated:
                    self.iter_n = i
                    break

    def plot_image(self, print_mode: int) -> None:
        """plot_image(self, print_mode: int) -> None:
        Plots all planets trajectory in a graph, where the scale of both axis is the same.
            For print_mode = 1 plots a curve for all planets with their actual position shown by a marker,
            for print_mode = 2 plots a number of points using the function plt.scatter, whose colors follow a certain colormap,
                which allows getting more information from the graph, such as start and end point (start is light, end is dark) or speed (from the color gradient).
        """
        fig, ax = plt.subplots()
        for i, planet in enumerate(self.planets):
            if print_mode == 1:
                color_name = COLORS[i % len(COLORS)]
                ax.plot(planet.trajectory[0,:self.iter_n], planet.trajectory[1,:self.iter_n], label=planet.name, color=color_name)
            if print_mode == 2:
                color = linspace(0,10,self.iter_n)
                cmap_name = CMAPS[i % len(CMAPS)]
                ax.scatter(planet.trajectory[0,:self.iter_n], planet.trajectory[1,:self.iter_n], cmap=cmap_name, c=color, marker=".", label=f"{planet.name}")
        ax.legend()
        if print_mode==1: 
            for i, planet in enumerate(self.planets):
                color_name = COLORS[i % len(COLORS)]
                ax.plot(planet.trajectory[0,self.iter_n-1], planet.trajectory[1,self.iter_n-1], label=planet.name, marker="o", color=color_name)
        ax.axis('equal')      
        plt.show()

    def plot_video(self, output_file: str = "animation.gif") -> None:
        """plot_video(self) -> None:
        Creates a 10s .gif animation of the planets movement using FuncAnimation from matplotlib."""
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        def animate(frame):
            plt.cla()
            for planet in self.planets:
                    ax.plot(planet.trajectory[0,:frame*10], planet.trajectory[1,:frame*10], label=f"{planet.name}")
            plt.legend()
        anim = FuncAnimation(fig=fig, func=animate, frames=int(self.iter_n/10), interval=10000/int(self.iter_n/10))
        anim.save(output_file, writer="PillowWriter")