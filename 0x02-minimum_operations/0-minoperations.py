#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """
    n: number

    return: fewest number of operations needed
    """
    ans: int = 0
    while n % 2 == 0:
        ans += 2
        n /= 2
    if n == 1:
        return ans

    from math import sqrt
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            ans += i + int(n / i) + 1
            print(i)
            return ans

    return int(ans + n)
