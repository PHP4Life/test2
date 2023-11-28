import random
import matplotlib.pyplot as plt

from planet import Planet
from robot import Robot
from human import Human


class Universe:

    def __init__(self):
        self.planets = []

    def generate(self, planet_name):
        planet1 = Planet()
        planet1.add_inhabitant(random.randrange(0, 100))
        self.planets.append(planet1)

    def show_populations(self, selection):
        x_values = []
        y_values = []

        num_humans = 0

        for planet in self.planets:
            x_values.append(planet.name)

            if selection == "humans":
                y_values.append(len(planet.inhabitants['humans']))
            else:
                y_values.append(len(planet.inhabitants['robots']))

        for inhabitant in self.planets.inhabitants:
            if isinstance(inhabitant, Human):
                num_humans += 1

        plt.bar(x_values, y_values)
        plt.tight_layout()
        plt.show()

    def __str__(self):
        return f'{self.planets}'
