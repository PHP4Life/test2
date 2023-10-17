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


listen()
identify()
escape_by(input("Enter a way to escape the boulder"))
