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

    # outputs should be at least 2 char: (min, Copy All => Paste)
    if n < 2:
        return 0
    operations, root = 0, 2
    while root <= n:
        if n % root == 0:
            operationss += root
            # set n to the remainder
            n = n / root
            root -= 1
        root += 1
    return operations
