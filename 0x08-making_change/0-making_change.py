#!/usr/bin/python3
""" Module for calculating the minimum number of coins
    needed to make a specific amount.
"""


def makeChange(coins, total):
    """ Returns the minimum number of coins needed
        to make the given total
    """
    dp = [0] + [total + 1] * total

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin < 0:
                continue
            dp[i] = min(dp[i - coin] + 1, dp[i])

    if dp[total] > total:
        return -1
    return dp[total]
