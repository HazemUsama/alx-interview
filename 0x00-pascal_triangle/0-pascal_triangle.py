#!/usr/bin/python3
"""Calculate the Pascal Triangle"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    ans = [[1]]
    for r in range(1, n, 1):
        row = []
        row.append(1)
        for c in range(1, r, 1):
            row.append(ans[r - 1][c - 1] + ans[r - 1][c])
        row.append(1)
        ans.append(row)
    return ans
