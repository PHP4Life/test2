class Human:
    MAX_ENERGY = 100

    # Constructor
    def __init__(self, name="Human", energy=MAX_ENERGY):
        self.name = name
        self.age = 0
        self.energy = energy

    def __repr__(self):
        return f'(name={self.name}, age={self.age})'

    def __str__(self):
        return f'{self.name} is {self.age} years old.'

    def grow(self):
        self.age += 1

    def eat(self, amount):
        if self.energy + amount > self.MAX_ENERGY:
            print("Energy is full")
        else:
            self.energy += amount

    def move(self, distance):
        if self.energy == 0:
            print("unable to move, eat to gain more energy")
        else:
            self.energy -= distance

    def display(self):
        print(f"I am {self.name}")
