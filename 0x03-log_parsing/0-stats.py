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
    status_codes = dict(sorted(status_codes.items(),
                               key=lambda item: item[1], reverse=True))
    for key, value in status_codes.items():
        print('{}: {}'.format(key, value))


pattern = r'(?P<status>\d{3}) (?P<size>\d+)$'
cnt = 0
total_size = 0
status_codes = {}
try:
    for line in sys.stdin:
        match = re.search(pattern, line)
        if match:
            status = int(match.group('status'))
            size = int(match.group('size'))
            cnt += 1
            total_size += size
            status_codes.setdefault(status, 0)
            status_codes[status] += 1

        if cnt == 10:
            statistics(total_size, status_codes)
            total_size = 0
            cnt = 0
            status_codes = {}

except KeyboardInterrupt:
    statistics(total_size, status_codes)
    sys.exit()
