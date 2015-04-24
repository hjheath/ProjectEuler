"""Problem 17 of https://projecteuler.net"""

import num2words


def problem_17():
    """Solution to problem 17."""
    answer = 0
    for number in range(1, 1001):
        word = num2words.num2words(number, lang='en_GB')
        no_spaces = word.replace(' ', '')
        no_hyphens = no_spaces.replace('-', '')
        answer += len(no_hyphens)

    return answer


if __name__ == '__main__':
    print(problem_17())
