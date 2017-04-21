"""Problem 21 of https://projecteuler.net"""

import projecteuler.maths_functions as maths


def problem_21():
    """Solution to problem 21."""
    amicable_numbers = []
    for number in range(1, 10000):
        if number in amicable_numbers:
            continue

        partner = sum(maths.get_divisor_list(number))
        partner_factor_sum = sum(maths.get_divisor_list(partner))

        # Amicable numbers paired with themselves (e.g. 6) are not allowed.
        if partner_factor_sum == number and partner != number:
            amicable_numbers.append(number)
            if partner < 10000:
                amicable_numbers.append(partner)

    answer = sum(amicable_numbers)
    return answer
