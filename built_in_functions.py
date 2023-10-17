# Functions

# Task 1 - ASCII Converter

def ascii_converter():
    print("Program Started!")
    character_input = input("Please enter a standard character: ")

    if len(character_input) != 1:
        print("Please enter a single character")

    ascii_number = ord(character_input)
    print(f"The character represented by the ASCII code {character_input} is {ascii_number}")


ascii_converter()
