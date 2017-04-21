"""Problem 42 of https://projecteuler.net"""

from itertools import takewhile
from pkg_resources import resource_string

from projecteuler.generators import triangle_numbers


# Assume no word is longer than 20 letters
TRIANGLES = [x for x in takewhile(lambda x: x < 520, triangle_numbers())]


def problem_42():
    """Solution to problem 42."""
    file_contents = resource_string('projecteuler.data', 'problem_42.dat')
    file_as_string = file_contents.decode('utf-8')
    words = file_as_string.replace('"', '').split(',')

    count = 0
    for word in words:
        if triangle_word(word):
            count += 1
    return count


def triangle_word(word):
    """Check if a word is a triangle word"""
    return sum([ord(character) - 64 for character in word]) in TRIANGLES
