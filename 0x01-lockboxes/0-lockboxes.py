#!/usr/bin/python3
"""determines if all the boxes can be opened"""
from collections import deque


def canUnlockAll(boxes):
    """Return True if all boxes can be unlocked"""
    n = len(boxes)
    queue = deque()

    if n == 0:
        return True

    opened = {0}
    queue.append(0)

    while (queue):
        box = boxes[queue.popleft()]

        for key in box:
            if key < n and key not in opened:
                queue.append(key)
                opened.add(key)

    return len(opened) == n
