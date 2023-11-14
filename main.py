import matplotlib.pyplot as plt


# Using Third-Party Libraries

# Task 1 - Basic line graph

def display_line(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.show()


def run_task():
    x_values = [1, 2, 3, 4, 5] # Values for the x-axis
    y_values = [1, 4, 9, 16, 25] # Values for the y-axis
    display_line(x_values, y_values)


run_task()
