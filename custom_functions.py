# Custom Functions

# Task 1 - Text adventure game

def listen():
    sound = input("Enter a word representing a sound: ")
    print(f"That was a loud {sound}!")


def identify():
    identify_object = input("Enter a word representing what they see: ")
    if identify_object == "a large boulder":
        print("It's time to run!")
    else:
        print("We will be fine")


def escape_by(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "cross bridge ahead":
        print("That might just work! Let's go!")
    else:
        print("We cannot escape that way! The boulder is in the way!")


def cross_bridge(steps):
    for crossing in range(steps):
        print("Crossed step.")
    if steps > 5:
        print("The bridge is collapsing!")
    print("we must keep going!")


def climb_ladder(steps_remaining, number_of_steps):
    if steps_remaining > number_of_steps:
        print("Still some way to go!")
    else:
        print("We are almost there!")


listen()
identify()
escape_by(input("Enter a way to escape the boulder: "))
cross_bridge(input("Enter how many steps over the bridge: "))
climb_ladder(10, 5)
