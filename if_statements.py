
# Task 1 - Print book type
book = input("Enter the type of book: ")

if book == "adventure": # Checks if the variable $book is equal to "adventure"
    print("I like adventure books!")

print("Finished reading book!")


# Task 2 - If & Else statements
activity = input("Please enter the activity to be performed:")

if activity == "calculate": # Checks if the variable $activity is equal to "calculate"
    print("Performing calculation")
else:
    print("Performing activity")

print("Activity completed")


# Task 3 - If...Elif...Else statement
direction = input("Enter the direction the robot should move (i.e. up, down, left or right):")

if direction == "up":
    print("I am moving in an upward direction!")
elif direction == "down":
    print("I am moving in a downward direction!")
elif direction == "left":
    print("I am moving left")
elif direction == "right":
    print("I am moving right")
else:
    print("I am stationary")


# Task 4 - Modulo Operator
number = input("Enter a number to determine whether it is odd or even:")

if int(number) % 2 == 0:
    print("even")
else:
    print("odd")