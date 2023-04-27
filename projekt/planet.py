import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

GRAV_CONST = 6.674e-11

class Planet:
    def __init__(self, name: str, pos, vel, mass: float, iter_n: int):
        self.name = name
        self.mass = mass
        self.vel = np.array([vel[0], vel[1]])
        self.coords = np.array([pos[0], pos[1]])
        self.accel = np.zeros((2))
        self.trajectory = np.zeros((2,iter_n))
        self.container_size = 5*np.linalg.norm(self.coords)
    
    @classmethod
    def random(cls, name: str, max_distance: float, max_speed: float, mass: float, iter_n: int):
        pos = np.random.uniform(low=-max_distance, high=max_distance, size=2)
        vel = np.random.uniform(low=-max_speed, high=max_speed, size=2)
        return cls(name, pos, vel, mass, iter_n)

    def __str__(self):
        return f"""Planet name: {self.name}
Planet mass: {self.mass}
Planet velocity: {self.vel}
Planet acceleration: {self.accel}
Current coords: {self.coords[0]}, {self.coords[1]}"""
    
    def get_acceleration(self, other):
        distance = np.linalg.norm(other.coords - self.coords)
        force = (GRAV_CONST*self.mass*other.mass)/(distance**2)
        dxdy = other.coords - self.coords
        self.accel += force*dxdy/(distance*self.mass)
        other.accel += -force*dxdy/(distance*other.mass)

    def update_coords(self, planets, i, dt):
        for j in range(len(planets)):
            planets[j].accel = 0
        for j in range(len(planets)):
            for k in range(j+1, len(planets)):
                Planet.get_acceleration(planets[j], planets[k])
        for planet in planets:
            planet.vel += planet.accel*dt
            planet.coords += planet.vel*dt
            planet.trajectory[:,i] = planet.coords[:]
        
    def is_too_far(self):
        distance = np.linalg.norm(self.coords)
        if distance > self.container_size:
            return True
        else:
            return False