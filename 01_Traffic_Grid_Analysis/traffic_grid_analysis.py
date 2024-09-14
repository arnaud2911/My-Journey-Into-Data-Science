# traffic_grid_analysis.py

import random

def initialize_traffic_grid(rows, cols, min_vehicles=0, max_vehicles=20):
    """
    Initializes a 2D traffic grid with random vehicle counts.

    Parameters:
        rows (int): Number of rows in the grid.
        cols (int): Number of columns in the grid.
        min_vehicles (int): Minimum number of vehicles at an intersection.
        max_vehicles (int): Maximum number of vehicles at an intersection.

    Returns:
        list: A 2D list representing the traffic grid.
    """
    grid = []
    for _ in range(rows):
        row = [random.randint(min_vehicles, max_vehicles) for _ in range(cols)]
        grid.append(row)
    return grid

def print_grid(grid, title="Grid"):
    """
    Prints the grid in a formatted way.

    Parameters:
        grid (list): The 2D list to print.
        title (str): Title of the grid.
    """
    print(f"\n{title}:")
    for row in grid:
        print(row)

