## Nested Loops

# Task 1 - display a grid of ASCII emojis
rows = input("How many rows should I have? ")
columns = input("How many columns should I have? ")

for numberOfRows in range(int(rows)):
    for numberOfColumns in range(int(columns)):
        print(":-)", end=" ")
    print("  ")

# Task 2 - enter a sequence of characters consisting of dashes and two markers
sequence = input()
marker = input("Enter a character representing a marker: ")
