#!/usr/bin/python3
"""
Log parsing script, reads from stdin and computes metrics.
"""
import sys


def print_stats(file_size, status_codes):
    """
    Prints the metrics.
    """
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 9:
            continue

        try:
            file_size += int(parts[-1])
        except ValueError:
            continue

        try:
            status_code = int(parts[-2])
            if status_code in status_codes:
                status_codes[status_code] += 1
        except ValueError:
            continue

        line_count += 1

        if line_count % 10 == 0:
            print_stats(file_size, status_codes)

except KeyboardInterrupt:
    print_stats(file_size, status_codes)
    raise

print_stats(file_size, status_codes)
