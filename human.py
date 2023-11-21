
class Human:
    MAX_ENERGY = 100

    # Constructor
    def __init__(self, name = "Human"):
        self.name = name
        self.age = 0
        self.energy = MAX_ENERGY

    def display(self):
        print(f"I am {self.name}")