from human import Human
from robot import Robot


class Planet:

    def __init__(self):
        self.inhabitants = {
            'humans': [],
            'robots': []
        }
     #  self.humans = []
     #  self.robots = []
        self.name = "Mecury"

    def add_human(self, human):
        self.inhabitants['humans'].append(human)

    def remove_human(self, human):
        self.inhabitants['humans'].remove(human)

    def add_robot(self, robot):
        self.inhabitants['robots'].append(robot)

    def remove_robot(self, robot):
        self.inhabitants['robots'].remove(robot)

    def __repr__(self):
        return f'(Welcome to {self.name}, there are {self.inhabitants["humans"]} humans & {self.inhabitants["robots"]} robots.)'

    def __str__(self):
        return f'Welcome to {self.name}, there are {self.inhabitants["humans"]} humans & {self.inhabitants["robots"]} robots.'



