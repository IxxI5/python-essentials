# Data Visualization with Matplotlib
# Matplotlib is a popular library for creating data visualization in Python.

# Install matplotlib and numpy (before using it) via terminal: pip install matplotlib numpy

# Import Matplotlib and Numpy library
import matplotlib.pyplot as plt
import numpy as np

# Example 1: Simple Line Plot
def simple_line_plot():
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    plt.plot(x, y)
    plt.title('Simple Line Plot')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.show()

# Example 2: Multiple Lines Plot
def multiple_lines_plot():
    x = [1, 2, 3, 4, 5]
    y1 = [1, 4, 9, 16, 25]
    y2 = [2, 5, 8, 11, 14]
    plt.plot(x, y1, label='Line 1')
    plt.plot(x, y2, label='Line 2')
    plt.title('Multiple Lines Plot')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.show()

# Example 3: Scatter Plot
def scatter_plot():
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    plt.scatter(x, y)
    plt.title('Scatter Plot')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.show()

# Example 4: Bar Chart
def bar_chart():
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    plt.bar(x, y)
    plt.title('Bar Chart')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.show()

# Advanced Example 1: Customized Plot
def customized_plot():
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    plt.plot(x, y, color='red', linestyle='--', marker='o')
    plt.title('Customized Plot')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.grid(True)
    plt.annotate('Point 1', xy=(1, 1), xytext=(1.1, 1.1), arrowprops=dict(facecolor='black', shrink=0.05))
    plt.show()

# Advanced Example 2: Coincidence Points
def coincidence_points_plot():
    # Define the functions
    def y1(x):
        return x**2 + 4

    def y2(x):
        return 2*x + 2

    # Generate x values
    x = np.linspace(-10, 10, 400)

    # Calculate y values
    y1_values = y1(x)
    y2_values = y2(x)

    # Find coincidence points
    coincidence_points = x[np.argwhere(np.diff(np.sign(y1_values - y2_values))).flatten()]

    # Plot the functions
    plt.plot(x, y1_values, label='y1 = x^2 + 1')
    plt.plot(x, y2_values, label='y2 = 2x + 2')

    # Plot the coincidence points
    plt.scatter(coincidence_points, y1(coincidence_points), color='red', label='Coincidence Points')

    # Add title and labels
    plt.title('Plot of y1 and y2 with Coincidence Points')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

# Run the examples
plt.ion()       # Enable interactive mode

simple_line_plot()
plt.pause(2)    # Show for 2 seconds

multiple_lines_plot()
plt.pause(2)    # Show for 2 seconds

scatter_plot()
plt.pause(2)    # Show for 2 seconds

bar_chart()
plt.pause(2)    # Show for 2 seconds

customized_plot()
plt.pause(2)

coincidence_points_plot()
plt.pause(2)    # Show for 2 seconds

plt.ioff()      # Disable interactive mode
plt.show()      # Ensure the last plot remains open

# Run the examples: 
# On closing the first displayed example, runs the next one automatically and so on due to default blocking mode. 
# simple_line_plot()
# multiple_lines_plot()
# scatter_plot()
# bar_chart()
# customized_plot()
# coincidence_points_plot()