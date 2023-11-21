# Week 9 - Object Oriented Programming
from human import Human
from robot import Robot

if __name__ == "__main__":
    human1 = Human()
    human1.display()
    print(human1)
    print(repr(human1))

    robot1 = Robot()
    robot1.display()
    print(robot1)
    print(repr(robot1))
