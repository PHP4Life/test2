# Week 9 - Object Oriented Programming
from human import Human
from robot import Robot
from planet import Planet
from universe import Universe

if __name__ == "__main__":
    human1 = Human()
    human1.display()
    human1.move(10)
    print(human1)
    print(repr(human1))

    robot1 = Robot()
    robot1.display()
    print(robot1)
    print(repr(robot1))

    planet1 = Planet()
    planet1.add_inhabitant(5)
    planet1.add_inhabitant(5)
    print(repr(planet1))

    universe1 = Universe()
    universe1.generate("hello")
    print(universe1)
    print("hello")
