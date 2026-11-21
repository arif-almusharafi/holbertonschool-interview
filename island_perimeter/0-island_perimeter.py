#!/usr/bin/python3
"""Module that calculates the perimeter of an island in a grid."""


def island_perimeter(grid):
    """Return the perimeter of the island described in grid.

    grid is a list of list of integers:
        0 represents water
        1 represents land
    """
    perimeter = 0
    rows = len(grid)

    for i in range(rows):
        cols = len(grid[i])
        for j in range(cols):
            if grid[i][j] == 1:
                # up
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # down
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
