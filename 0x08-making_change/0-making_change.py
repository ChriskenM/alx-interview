#!/usr/bin/python3
"""
function Return: fewest number of coins needed to meet total
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total
    :param coins: List of the values of the coins in your possession
    :param total: The total amount to meet
    :return: The fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
