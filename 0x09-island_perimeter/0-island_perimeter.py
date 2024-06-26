#!/usr/bin/python3
def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    :param grid: List of list of integers representing the grid
    :return: Perimeter of the island
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check the four directions
                if r == 0 or grid[r-1][c] == 0:  # Top
                    perimeter += 1
                if r == rows - 1 or grid[r+1][c] == 0:  # Bottom
                    perimeter += 1
                if c == 0 or grid[r][c-1] == 0:  # Left
                    perimeter += 1
                if c == cols - 1 or grid[r][c+1] == 0:  # Right
                    perimeter += 1

    return perimeter
