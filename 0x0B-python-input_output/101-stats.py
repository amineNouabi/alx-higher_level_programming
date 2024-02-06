#!/usr/bin/python3

"""

Defines a script that reads stdin line by line and computes metrics.

"""


import sys

status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}


def print_stats(file_size):
    """Prints the status codes and file size.

    Args:
        file_size (int): total file size
    """
    print("File size: {:d}".format(file_size))
    for code, count in sorted(status_codes.items()):
        if count:
            print("{:s}: {:d}".format(code, count))


def main():
    """Reads stdin line by line and computes metrics."""
    file_size = 0
    line_count = 0
    try:
        for line in sys.stdin:
            line_count += 1
            split = line.split()
            try:
                status = split[-2]
                if status in status_codes:
                    status_codes[status] += 1
            except BaseException:
                pass
            try:
                file_size += int(split[-1])
            except BaseException:
                pass
            if line_count % 10 == 0:
                print_stats(file_size)
    except KeyboardInterrupt:
        pass
    finally:
        print_stats(file_size)


if __name__ == "__main__":
    main()
