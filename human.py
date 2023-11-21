
class Human:
    MAX_ENERGY = 100

    # Constructor
    def __init__(self, name="Human", energy=MAX_ENERGY):
        self.name = name
        self.age = 0
        self.energy = energy

    def display(self):
        print(f"I am {self.name}")