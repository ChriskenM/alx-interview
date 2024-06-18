#!/usr/bin/python3
"""
function Return: fewest number of coins needed to meet total
"""
from collections import deque


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total
    :param coins: List of the values of the coins in your possession
    :param total: The total amount to meet
    :return: The fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order
    queue = deque([(0, 0)])  # (current_amount, number_of_coins_used)
    visited = set()  # To keep track of visited amounts

    while queue:
        current_amount, num_coins = queue.popleft()

        for coin in coins:
            next_amount = current_amount + coin
            if next_amount == total:
                return num_coins + 1
            if next_amount < total and next_amount not in visited:
                visited.add(next_amount)
                queue.append((next_amount, num_coins + 1))

    return -1
