import random

from planet import Planet


class Universe:

    def __init__(self):
        self.planets = []

    def generate(self, planet_name):
        planet1 = Planet()
        planet1.add_human(random.randrange(0, 100))
        planet1.add_robot(random.randrange(0, 100))
        self.planets.append(planet1)

    def __str__(self):
        return f'{self.planets}'
