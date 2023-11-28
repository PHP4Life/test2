from tech import Tech
from inhabitant import Inhabitant


class Alien(Inhabitant):

    def __init__(self):
        self.technology = []

    def pickup(self, tech):
        self.technology.append(tech)

    def drop(self, tech):
        self.technology.remove(tech)
