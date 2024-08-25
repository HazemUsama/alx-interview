#!/usr/bin/python3
""" Module for calculating the minimum number of coins
    needed to make a specific amount.
"""



def makeChange(coins, total):
    """ Returns the minimum number of coins needed
        to make the given total
    """
    cache = {}

    def helper(total):
        if total <= 0:
            return 0

        ans = -1
        for coin in coins:
            target = total - coin
            if target == 0:
                return 1
            elif target < 0:
                continue
            if target not in cache:
                cache[target] = helper(target)

            if cache[target] == -1:
                continue

            if ans == -1:
                ans = cache[target]
            ans = min(ans, cache[target])

        if ans > 0:
            ans += 1
        return ans

    return helper(total)
