
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


# # Task 3 - If...Elif...Else statement
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


# # Task 4 - Modulo Operator
number = input("Enter a number to determine whether it is odd or even:")

if int(number) % 2 == 0:
    print("even")
else:
    print("odd")


# Task 5 - Comparison Operators
numberC1 = input("Enter your first number:")
numberC2 = input("Enter your second number:")

if int(numberC1) < int(numberC2):
    print("The first number is the smallest")
elif int(numberC1) > int(numberC2):
    print("The second number is the smallest")
else:
    print("Both are equal")

# Task 6 - Counter to keep track of odd or even numbers
numberW1 = input("Enter your first number:")
numberW2 = input("Enter your second number:")
numberW3 = input("Enter your third number:")

oddCounter = 0
evenCounter = 0

if int(numberW1) % 2 == 0:
    evenCounter += 1
else:
    oddCounter += 1

if int(numberW2) % 2 == 0:
    evenCounter += 1
else:
    oddCounter += 1

if int(numberW3) % 2 == 0:
    evenCounter += 1
else:
    oddCounter += 1

print(f"There are {evenCounter} even and {oddCounter} odd numbers")
