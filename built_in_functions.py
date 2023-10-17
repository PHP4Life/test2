# Functions

# Task 1 - Character to ASCII Converter
def ascii_converter():
    print("Program Started!")
    character_input = input("Please enter a standard character: ")

    if len(character_input) != 1:
        print("Please enter a single character")

    ascii_number = ord(character_input)
    print(f"The character represented by the ASCII code {character_input} is {ascii_number}")


ascii_converter()


# Task 2 - ASCII to Character Converter
def character_converter():
    print("Program Started!")
    ascii_input = input("Please enter an ASCII code: ")

    character = chr(int(ascii_input))
    print(f"The character represented by the ASCII code {ascii_input} is {character}")


character_converter()
