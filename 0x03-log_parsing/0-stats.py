#!/usr/bin/python3
"""
Script, reads stdin line by line and computes metrics.
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


def parse_line(line, status_codes):
    """
    Parses a single line to extract file size and status code.
    """
    try:
        parts = line.split()
        file_size = int(parts[-1])
        status_code = parts[-2]
        if status_code in status_codes:
            status_codes[status_code] += 1
        return file_size
    except (IndexError, ValueError):
        return 0


if __name__ == "__main__":
    status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    file_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            file_size += parse_line(line, status_codes)
            line_count += 1
            if line_count % 10 == 0:
                print_stats(file_size, status_codes)
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise

    print_stats(file_size, status_codes)
