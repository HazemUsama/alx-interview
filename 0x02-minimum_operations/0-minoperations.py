#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """
    n: number

    return: fewest number of operations needed
    """
    if n < 4:
        if n <= 1:
            return 0
        return n

    div = []
    from math import sqrt
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            div.append(i)
            if i != n / i:
                div.append(int(n / i))
    ans = div[0]
    curr = div[0]
    for i in range(len(div)):
        if div[i] % curr == 0 and curr != div[i]:
            ans += div[i] / curr
            curr = div[i]
    ans += n / curr
    return int(ans)
