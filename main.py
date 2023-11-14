import matplotlib.pyplot as plt


# Using Third-Party Libraries

# Activity 1, Task 1 - Basic line graph

def display_line(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.show()


def run_task1():
    x_values = [1, 2, 3, 4, 5] # Values for the x-axis
    y_values = [1, 4, 9, 16, 25] # Values for the y-axis
    display_line(x_values, y_values)


# run_task1()

# Task 2 - Display multiple graphs

def small():
    x = [3, 3, 4, 4, 3]
    y = [3, 4, 4, 3, 3]
    plt.plot(x, y, 'ro:')


def medium():
    x = [2, 2, 5, 5, 2]
    y = [2, 5, 5, 2, 2]
    plt.plot(x, y, 'gs--')


def large():
    x = [1, 1, 1, 6, 6, 1, 6]
    y = [1, 6, 6, 6, 1, 1, 1]
    plt.plot(x, y, 'bp-')


def run_task2():
    small()
    medium()
    large()
    plt.show()


run_task2()

# Task 3 -

def coordinate():
    x = input("Enter an x-axis value")
    y = input("Enter an y-axis value")

    return x, y


def path():
    print("Retrieving path...")

    x_values = []
    y_values = []

    for i in range(4):

## To complete later.




def run_task3():

