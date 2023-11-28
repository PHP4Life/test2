from inhabitants.inhabitant import Inhabitant


class Robot(Inhabitant):
    MAX_ENERGY = 100
    laws = "Protect, Obey and Survive"

    # Constructor
    def __init__(self, name="Robot", energy=0):
        super.name = name
        super.age = 0
        super.energy = energy

    @staticmethod
    def the_laws():
        print(Robot.laws)

    def __repr__(self):
        return f'(name={self.name}, age={self.age})'

    def __str__(self):
        return f'{self.name} is {self.age} years old.'

    def display(self):
        print(f"I am {self.name}")
