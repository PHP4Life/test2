## For Loops

# Task 1 - Display mountains
mountains = input("How many mountains should I display? ")

for mountainsASCII in range(int(mountains)):
    print("      __")
    print("     /  \_")
    print("    /^    \ ")
    print("   /  ^    \_")
    print(" _/ ^ ^     ^\ ")
    print("_/ ^ ^     ^\ ")

# Task 2 - How far are we from the target?
distance = input("How far are we from the target? ")
target = 0

for target in range(int(distance)):
    target += 1
    print(target, "steps remaining")

print("Target achieved!")

# Task 3 - Level of brightness
brightness = input("What level of brightness is required? ")
initial = 0
level = ""

for initial in range(int(brightness)):
    initial += 1
    level = level + "*"
    print("Brightness level:", level)

print("Complete!")