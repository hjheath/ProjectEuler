"""Problem 11 of https://projecteuler.net"""

from pkg_resources import resource_string
from projecteuler.maths_functions import multiply


def problem_11():
    """Solution to problem 11."""
    file_conents = resource_string('projecteuler.data', 'problem_11.dat')
    file_as_string = file_conents.decode('utf-8')
    lines = file_as_string.split('\n')
    grid = [line.split(' ') for line in lines]
    grid = [[int(entry) for entry in line] for line in grid]
    highest_product = 0

    # Horizontal sum.
    for y_value in range(0, 20):
        for x_value in range(0, 17):
            product = multiply(grid[y_value][x_value: x_value + 3])
            highest_product = max(product, highest_product)

    # Vertical sum.
    for y_value in range(0, 17):
        for x_value in range(0, 20):
            adjacent_numbers = [grid[y_value + i][x_value] for i in
                                range(0, 4)]
            product = multiply(adjacent_numbers)
            highest_product = max(product, highest_product)

    # Diagonal down to the right sum.
    for y_value in range(0, 17):
        for x_value in range(0, 17):
            adjacent_numbers = [grid[y_value + i][x_value + i] for i in
                                range(0, 4)]
            product = multiply(adjacent_numbers)
            highest_product = max(product, highest_product)

    # Diagonal down to the left sum.
    for y_value in range(0, 17):
        for x_value in range(3, 20):
            adjacent_numbers = [grid[y_value + i][x_value - i] for i in
                                range(0, 4)]
            product = multiply(adjacent_numbers)
            highest_product = max(product, highest_product)

    return highest_product

if __name__ == '__main__':
    print(problem_11())
