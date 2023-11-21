# Week 9 - Object Oriented Programming
from human import Human
from robot import Robot
from planet import Planet

if __name__ == "__main__":
    human1 = Human()
    human1.display()
    print(human1)
    print(repr(human1))

    robot1 = Robot()
    robot1.display()
    print(robot1)
    print(repr(robot1))

    planet1 = Planet()
    planet1.add_human(5)
    planet1.add_robot(5)
    print(repr(planet1))
