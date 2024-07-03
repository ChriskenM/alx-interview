#!/usr/bin/python3
"""
Determines the winner of each game between Maria and Ben
"""


def isWinner(x, nums):
    """
    Determines the winner of each game between Maria and Ben.
    :param x: Number of rounds.
    :param nums: List of n values for each round.
    :return: Name of the player with the most wins, or None if there's a tie.
    """
    if x < 1 or not nums:
        return None

    # Find the maximum number in nums to limit the sieve size
    max_n = max(nums)

    # Sieve of Eratosthenes to find all primes up to max_n
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    for start in range(2, int(max_n**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, max_n + 1, start):
                sieve[multiple] = False

    # Precompute the number of primes up to each number
    prime_count = [0] * (max_n + 1)
    count = 0
    for i in range(max_n + 1):
        if sieve[i]:
            count += 1
        prime_count[i] = count

    # Determine the winner for each game
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
