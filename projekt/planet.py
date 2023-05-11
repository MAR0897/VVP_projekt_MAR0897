"""
Module with class Planet
"""

import numpy as np
from typing import List

GRAV_CONST: float = 6.674e-11


class Planet:
    """
    Represents a planet/object with name, mass, velocity, acceleration and coordinates.
    Stores its position over time in trajectory variable which is then used for graphs or animation.
    Variables:
        name: str
        mass: float
        vel: ndarray
        coords: ndarray
        accel: ndarray
        trajectory: ndarray
        container_size: float
    Methods:
        __str__(self) -> str:
    """
    def __init__(self, name: str, pos: list, vel: list, mass: float, iter_n: int, random: bool) -> None:
        """__init__(self, name: str, pos: np.ndarray, vel: np.ndarray, mass: float, iter_n: int) -> None:
        Reads initial values of the planet parameters from JSON file.
        """
        self.name = name
        self.mass = mass
        self.vel = np.array([vel[0], vel[1]])
        self.coords = np.array([pos[0], pos[1]])
        if random:
            self.vel = np.random.uniform(low=-np.linalg.norm(self.vel), high=np.linalg.norm(self.vel), size=2)
            self.coords = np.random.uniform(low=-np.linalg.norm(self.coords), high=np.linalg.norm(self.coords), size=2)
        self.accel = np.zeros((2))
        self.trajectory = np.zeros((2, iter_n))
        self.container_size = 10*np.linalg.norm(self.coords)

    def __str__(self) -> str:
        """__str__(self) -> str:
        Prints current planet parameters values.
        """
        return f"""Planet name: {self.name}
Planet mass: {self.mass}
Planet velocity: {self.vel}
Planet acceleration: {self.accel}
Current coords: {self.coords[0]}, {self.coords[1]}"""

    def get_acceleration(self, other: "Planet") -> None:
        """get_acceleration(self, other: "Planet") -> None:
        Computes acceleration of a pair of planets.
            1. Calculates distance between the two planets.
            2. Calculates force (F = G*m1*m2/r^2, where G is the gravitational constant).
            3. Calculates the acceleration.
        """
        distance = np.linalg.norm(other.coords - self.coords)
        force = (GRAV_CONST*self.mass*other.mass)/(distance**2)
        dxdy = other.coords - self.coords
        self.accel += force*dxdy/(distance*self.mass)
        other.accel += -force*dxdy/(distance*other.mass)

    def update_coords(self, planets: List["Planet"], i: int, dt: float) -> None:
        """update_coords(self, planets: List["Planet"], i: int, dt: float) -> None:
        Updates the position of all planets in a single iteration.
            1. Sets acceleration of all planets to zero.
            2. Calculates the acceleration between all pairs of planets.
            3. Updates the valocity and position.
        """
        for j in range(len(planets)):
            planets[j].accel = 0
        for j in range(len(planets)):
            for k in range(j+1, len(planets)):
                Planet.get_acceleration(planets[j], planets[k])
        for planet in planets:
            planet.vel += planet.accel*dt
            planet.coords += planet.vel*dt
            planet.trajectory[:, i] = planet.coords[:]

    def is_too_far(self) -> bool:
        """is_too_far(self) -> bool
        Checks if the simulation has degenerated (at least one of the planets got too far to visibly interact with other planets).
        The "too far" is set as a spherical container 10x the initial distance of the planet from the point (0,0). 
        Checks every 100 iterations.
        Checking can be turned on by setting the variable container to 1.
        """
        distance = np.linalg.norm(self.coords)
        if distance > self.container_size:
            return True
        else:
            return False
