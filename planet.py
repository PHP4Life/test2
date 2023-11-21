from human import Human
from robot import Robot


class Planet:

    def __init__(self):
        self.humans = []
        self.robots = []
        self.name = "Mecury"

    def add_human(self, human):
        self.humans.append(human)

    def remove_human(self, human):
        self.humans.remove(human)

    def add_robot(self, robot):
        self.robots.append(robot)

    def remove_robot(self, robot):
        self.robots.remove(robot)

    def __repr__(self):
        return f'(Welcome to {self.name}, there are {self.humans} humans & {self.robots} robots.)'

    def __str__(self):
        return f'Welcome to {self.name}, there are {self.humans} humans & {self.robots} robots.'
