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


listen()
identify()
