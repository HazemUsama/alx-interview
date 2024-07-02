#!/usr/bin/python3
import sys


def safe(x, y):
    if row[x]:
        return False
    for i, j in placed:
        if abs(i - x) == abs(j - y):
            return False
    return True


def solve(c=0):
    if c == n:
        print(placed)
        return
    for r in range(n):
        if safe(r, c):
            row[r] = 1
            placed.append([r, c])
            solve(c + 1)
            row[r] = 0
            placed.pop()


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])

except ValueError:
    print("N must be a number")
    exit(1)

if n < 4:
    print("N must be at least 4")
    exit(1)

row = [0] * n
placed = []

solve()
