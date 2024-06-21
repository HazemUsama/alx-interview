#!/usr/bin/python3

import sys
import re


def statistics(total_size, status_codes):
    """
    Print the statistics of the log

    Args:
        total_size (int): The total size of the log
        status_codes (dict): The status codes of the log

    Returns: None
    """
    print('File size:', total_size)
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print('{}: {}'.format(key, value))


pt = (
    r'\s*(\S+)\s*',
    r'\s*\[(\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
    r'\s*"([^"]*)"\s*',
    r'\s*(?P<status>\S+)',
    r'\s*(?P<size>\d+)'
)
pattern = '{}\\-{}{}{}{}\\s*'.format(pt[0], pt[1], pt[2], pt[3], pt[4])
cnt = 0
total_size = 0
status_codes = {"200": 0,
                "301": 0,
                "400": 0,
                "401": 0,
                "403": 0,
                "404": 0,
                "405": 0,
                "500": 0}

try:
    for line in sys.stdin:
        line.strip()
        match = re.fullmatch(pattern, line)
        if match:
            status = match.group('status')
            size = int(match.group('size'))
            cnt += 1
            total_size += size
            if status in status_codes.keys():
                status_codes[status] += 1

        if cnt == 10:
            statistics(total_size, status_codes)
            cnt = 0

finally:
    statistics(total_size, status_codes)
