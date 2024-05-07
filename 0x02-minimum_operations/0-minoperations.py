#!/usr/bin/env python3
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
    if n <= 1:
        return n

    operations = 0
    for i in range(2, n + 1):
        while n % i == 0:
            operations += i
            n //= i
    return operations
