#!/usr/bin/python3
import sys
import re

pattern = (
    r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[(.*?)\] ".*?" '
    r'(?P<status>\d{3}) (?P<size>\d+)$'
)
cnt = 0
total_size = 0
status_codes = {}


def statistics(total_size, status_codes):
    print('File size:', total_size)
    status_codes = dict(sorted(status_codes.items(),
                               key=lambda item: item[1], reverse=True))
    for key, value in status_codes.items():
        print('{}: {}'.format(key, value))


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
