"""Problem 22 of https://projecteuler.net"""

from pkg_resources import resource_string


def problem_22():
    """Solution to problem 22."""
    file_contents = resource_string('projecteuler.data', 'problem_22.dat')
    file_as_string = file_contents.decode('utf-8')
    names = file_as_string.replace('"', '').split(',')
    names.sort()

    values = []
    for position, name in enumerate(names, start=1):
        value = position * sum([ord(character) - 64 for character in name])
        values.append(value)

    answer = sum(values)
    return answer


if __name__ == '__main__':
    print(problem_22())
