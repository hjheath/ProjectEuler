"""Problem 32 of https://projecteuler.net"""

from projecteuler.inspectors import pandigital_product


def problem_32():
    """Solution to problem 32."""
    product_list = []

    for multiplicand in range(1, 10):
        for multiplier in range(1000, 10000):
            product = pandigital_product(multiplicand, multiplier)
            if product:
                product_list.append(product)

    for multiplicand in range(10, 100):
        for multiplier in range(100, 1000):
            product = pandigital_product(multiplicand, multiplier)
            if product:
                product_list.append(product)

    answer = sum(set(product_list))
    return answer
