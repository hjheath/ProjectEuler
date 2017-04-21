"""Problem 19 of https://projecteuler.net"""

from calendar import weekday


def problem_19():
    """Solution to problem 19."""
    first_days = [weekday(year, month, 1) for year in range(1901, 2001) for
                  month in range(1, 13)]

    # An entry correpsonding to 6 denotes Sunday.
    answer = first_days.count(6)
    return answer
