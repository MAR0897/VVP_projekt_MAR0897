import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy import linspace
from typing import List
from planet import Planet

CMAPS = ["Blues", "Reds", "Greens", "Purples", "Oranges", "Greys"]

def plot(planets: List[Planet], print_mode: int, iter_n: int) -> None:
    if 0 <= print_mode <= 2:
        plot_image(planets, iter_n, print_mode)
    elif print_mode == 3:
        plot_video(planets, iter_n)
    else:
        raise ValueError("Invalid print_mode value!")
    
def plot_image(planets: List[Planet], iter_n: int, print_mode: int) -> None:
    fig, ax = plt.subplots()
    for i, planet in enumerate(planets):
        if print_mode == 0:
            ax.plot(planet.trajectory[0,:iter_n], planet.trajectory[1,:iter_n], label=f"{planet.name}")
        if print_mode == 1:
            if i == 0: 
                ax.plot(planet.trajectory[0,:iter_n], planet.trajectory[1,:iter_n], marker="o", markersize=5, color="orange", label=f"{planet.name}")
            else:
                ax.plot(planet.trajectory[0,:iter_n], planet.trajectory[1,:iter_n], label=f"{planet.name}")
        if print_mode == 2:
            color = linspace(0,10,iter_n)
            cmap_name = CMAPS[i % len(CMAPS)]
            ax.scatter(planet.trajectory[0,:iter_n], planet.trajectory[1,:iter_n], cmap=cmap_name, c=color, marker=".", label=f"{planet.name}")
    ax.axis('equal')
    ax.legend()
    plt.show()

def plot_video(planets: List[Planet], iter_n: int) -> None:
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    def animate(frame):
        plt.cla()
        for planet in planets:
                ax.plot(planet.trajectory[0,:frame], planet.trajectory[1,:frame], label=f"{planet.name}")
        plt.legend()
    anim = FuncAnimation(fig=fig, func=animate, frames=iter_n, interval=10000/iter_n)
    anim.save("animation.gif", writer="Pillow")

def plot_instant(planets: List[Planet], it: int) -> None:
    fig, ax = plt.subplots()
    for i, planet in enumerate(planets):
        ax.plot(planet.trajectory[0,it], planet.trajectory[1,it], marker="o", markersize=5, label=f"{planet.name}")
    ax.axis('equal')
    ax.legend()
    plt.show()