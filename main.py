import matplotlib.pyplot as plt


# Using Third-Party Libraries

# Activity 1, Task 1 - Basic line graph

def display_line(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.show()


# def run_task1():
#     x_values = [1, 2, 3, 4, 5] # Values for the x-axis
#     y_values = [1, 4, 9, 16, 25] # Values for the y-axis
#     display_line(x_values, y_values)
#
#
# run_task1()

# Task 2 -

def small():
    x = [3, 4, 3, 4, 3, 3, 4, 4]
    y = [3, 3, 4, 4, 3, 4, 3, 4]
    plt.plot(x, y, 'ro:')


def medium():
    x = [2, 5, 2, 5, 2, 2, 5, 5]
    y = [2, 2, 5, 5, 2, 5, 2, 5]
    plt.plot(x, y, 'gs--')


def large():
    x = [1, 6, 1, 6, 1, 1, 6, 6, 1, 6]
    y = [1, 6, 6, 6, 1, 6, 1, 6, 1, 1]
    plt.plot(x, y, 'bp-')


def run_task2():
    small()
    medium()
    large()
    plt.show()


run_task2()
