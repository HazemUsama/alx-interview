#!/usr/bin/python3
import sys
import re
import signal


pattern = (
    r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[(.*?)\] ".*?" '
    r'(?P<status>\d{3}) (?P<size>\d+)$'
)
cnt = 0
sum = 0
status_codes = {}


def statistics(total_size, status_codes):
    print('File size:', total_size)
    status_codes = dict(sorted(status_codes.items(),
                               key=lambda item: item[1], reverse=True))
    for key, value in status_codes.items():
        print('{}: {}'.format(key, value))


def interrupt_handler(signum, frame):
    statistics(sum, status_codes)
    sys.exit()


signal.signal(signal.SIGINT, interrupt_handler)


try:
    for line in sys.stdin:
        match = re.search(pattern, line)
        if match:
            status = int(match.group('status'))
            size = int(match.group('size'))
            cnt += 1
            sum += size
            status_codes.setdefault(status, 0)
            status_codes[status] += 1

        if cnt == 10:
            statistics(sum, status_codes)
            sum = 0
            cnt = 0
            status_codes = {}

except KeyboardInterrupt:
    statistics(sum, status_codes)
    sys.exit()
