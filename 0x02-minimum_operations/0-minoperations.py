#!/usr/bin/python3
"""
method that calculates the fewest number of operations needed,
    to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result,
     in exactly n 'H' characters in the file.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The fewest number of operations needed to reach,
                n 'H' characters.
             Returns 0 if n is impossible to achieve.
    """

    if type(n) is not int or n <= 1:
        return 0

    summation = []

    divisor = 2

    while (n % divisor) is 0 and (n // divisor) is not 1:
        summation.append(divisor)
        n = n // divisor

    divisor = 3

    while n > divisor:
        while (n % divisor) is 0 and (n // divisor) is not 1:
            summation.append(divisor)
            n = n // divisor

        divisor += 2

    summation.append(n)

    return sum(summation)
