"""Check for types of numbers."""


def is_palindrome(number):
    """
    Check if a number is a palindrome

    :param number: The int to check.
    """
    number_string = str(number)
    reversed_number = ''.join(reversed(number_string))
    return number_string == reversed_number
