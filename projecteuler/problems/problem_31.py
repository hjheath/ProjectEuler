"""Problem 31 of https://projecteuler.net"""


def problem_31():
    """Solution to problem 31."""
    coins = [200, 100, 50, 20, 10, 5, 2, 1]

    def combinations(total, coin_number):
        """
        A recursive function to find the number of ways to pay a total.

        :param total: An integer of the total to be paid.

        :param coin_number: The number of different coins available.

        :returns: The number of possible combinations.
        """
        # We hit our target - this is a valid combination.
        if total == 0:
            count = 1
        # We overshot our target - this cannot result in a valid combination.
        elif total < 0:
            count = 0
        # We ran out of coins - this cannot result in a valid combination.
        elif coin_number < 0 and total >= 1:
            count = 0

        # We have not yet hit the the target and we have coins remaining.
        # Use recursion to find the combinations using different coins, and the
        # combinations for a total reduced by the value of the current coin.
        else:
            count_with_different_coins = combinations(total, coin_number - 1)

            new_total = total - coins[coin_number]
            count_of_new_total = combinations(new_total, coin_number)

            count = count_with_different_coins + count_of_new_total

        return count

    answer = combinations(200, len(coins) - 1)
    return answer

if __name__ == '__main__':
    print(problem_31())
