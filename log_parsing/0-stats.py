#!/usr/bin/python3
"""Log parsing: reads stdin line by line and prints metrics."""
import sys


def print_stats(total_size, status_counts):
    """Print the total file size and the number of lines per status code."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    total_size = 0
    status_counts = {}
    valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            try:
                status = int(parts[-2])
                size = int(parts[-1])
            except (ValueError, IndexError):
                continue

            total_size += size
            if status in valid_codes:
                status_counts[status] = status_counts.get(status, 0) + 1

            count += 1
            if count % 10 == 0:
                print_stats(total_size, status_counts)
    finally:
        print_stats(total_size, status_counts)
