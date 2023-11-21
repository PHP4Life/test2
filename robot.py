
class Robot:
    MAX_ENERGY = 100

    # Constructor
    def __init__(self, name = "Robot", energy = 0):
        self.name = name
        self.age = 0
        self.energy = energy

    def __repr__(self):
        return f'(name={self.name}, age={self.age})'

    def __str__(self):
        return f'{self.name} is {self.age} years old.'

    def display(self):
        print(f"I am {self.name}")