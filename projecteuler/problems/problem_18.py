"""Problem 18 of https://projecteuler.net"""

from pkg_resources import resource_string


def problem_18():
    """Solution to problem 18."""
    file_conents = resource_string('projecteuler.data', 'problem_18.dat')
    file_as_string = file_conents.decode('utf-8')
    lines = file_as_string.split('\n')
    triangle = [line.split(' ') for line in lines]
    triangle = [[int(entry) for entry in line] for line in triangle]

    # Work up from the bottom. Remove the each row by adding the larger of
    # the two lowest row numbers to the number above them.
    triangle.reverse()
    for line in range(len(triangle) - 1):
        for entry in range(len(triangle[line]) - 1):
            triangle[line + 1][entry] += max(triangle[line][entry],
                                             triangle[line][entry + 1])

    # The answer is then the top entry of the triangle.
    triangle.reverse()
    answer = triangle[0][0]
    return answer

if __name__ == '__main__':
    print(problem_18())
