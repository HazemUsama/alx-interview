#!/usr/bin/python3
"""A module to check UTF-8 Validation"""


def validUTF8(data):
    """A function to check if a data set is a valid UTF-8 encoding"""
    n = len(data)
    i = 0

    while i < n:
        byte = data[i]

        if byte >> 7 == 0:
            num_bytes = 1
        elif byte >> 5 == 0b110:
            num_bytes = 2
        elif byte >> 4 == 0b1110:
            num_bytes = 3
        elif byte >> 3 == 0b11110:
            num_bytes = 4
        else:
            return False

        if i + num_bytes > n:
            return False
        for j in range(1, num_bytes):
            if data[i + j] >> 6 != 0b10:
                return False
        i += num_bytes

    return True
