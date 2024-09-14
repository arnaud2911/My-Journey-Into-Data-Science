# traffic_grid_analysis.py

"""
Traffic Grid Analysis

This script simulates traffic flow in a city grid and performs analyses such as:
- Calculating the total number of vehicles
- Identifying intersections with the highest traffic
- Transposing the grid
- Visualizing traffic density
- Processing real traffic data from external sources

Author: Arnaud PELAMA PELAMA TIOGO
Date: 1994-11-29
"""

import random
import csv
import matplotlib.pyplot as plt

def initialize_traffic_grid(rows=5, cols=5, min_vehicles=0, max_vehicles=20):
    """
    Initializes a 2D traffic grid with random vehicle counts.
    """
    grid = []
    for _ in range(rows):
        row = [random.randint(min_vehicles, max_vehicles) for _ in range(cols)]
        grid.append(row)
    return grid

def print_grid(grid, title="Grid"):
    """
    Prints the grid in a formatted way.
    """
    print(f"\n{title}:")
    for row in grid:
        print(' '.join(f"{value:2}" for value in row))

def calculate_total_vehicles(grid):
    """
    Calculates the total number of vehicles in the grid.
    """
    total = sum(sum(row) for row in grid)
    return total

def find_max_traffic_intersections(grid):
    """
    Finds the intersections with the highest number of vehicles.
    """
    max_vehicles = 0
    max_positions = []
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value > max_vehicles:
                max_vehicles = value
                max_positions = [(i, j)]
            elif value == max_vehicles:
                max_positions.append((i, j))
    return max_vehicles, max_positions

def transpose_grid(grid):
    """
    Transposes the given 2D grid.
    """
    transposed = [list(row) for row in zip(*grid)]
    return transposed

def visualize_traffic_density(grid, title="Traffic Density"):
    """
    Visualizes the traffic density using a heatmap.
    """
    plt.imshow(grid, cmap='hot', interpolation='nearest')
    plt.colorbar(label='Number of Vehicles')
    plt.title(title)
    plt.xlabel('Columns')
    plt.ylabel('Rows')
    plt.show()

def load_real_traffic_data(file_path):
    """
    Loads real traffic data from a CSV file.
    """
    grid = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            grid.append([int(value) for value in row])
    return grid

def main():
    # User input for grid size and vehicle count range
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    min_vehicles = int(input("Enter the minimum number of vehicles: "))
    max_vehicles = int(input("Enter the maximum number of vehicles: "))

    # Step 1: Initialize the traffic grid
    traffic_grid = initialize_traffic_grid(rows, cols, min_vehicles, max_vehicles)

    # Step 2: Print the traffic grid
    print_grid(traffic_grid, title="Traffic Grid")

    # Step 3: Calculate total number of vehicles
    total_vehicles = calculate_total_vehicles(traffic_grid)
    print(f"\nTotal number of vehicles in the grid: {total_vehicles}")

    # Step 4: Find and print intersections with the highest traffic
    max_vehicles, max_positions = find_max_traffic_intersections(traffic_grid)
    print(f"\nHighest number of vehicles at an intersection: {max_vehicles}")
    print("Intersection(s) with the highest traffic:")
    for position in max_positions:
        print(f" - Row {position[0]}, Column {position[1]}")

    # Step 5: Transpose the grid
    transposed_grid = transpose_grid(traffic_grid)

    # Step 6: Print the transposed grid
    print_grid(transposed_grid, title="Transposed Traffic Grid")

    # Step 7: Visualize the traffic density
    visualize_traffic_density(traffic_grid, title="Traffic Density")

    # Step 8: Load and process real traffic data (optional)
    real_data_file = input("Enter the path to the real traffic data CSV file (or press Enter to skip): ")
    if real_data_file:
        real_traffic_grid = load_real_traffic_data(real_data_file)
        print_grid(real_traffic_grid, title="Real Traffic Grid")
        visualize_traffic_density(real_traffic_grid, title="Real Traffic Density")

if __name__ == "__main__":
    main()