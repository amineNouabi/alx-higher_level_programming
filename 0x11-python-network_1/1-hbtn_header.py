#!/usr/bin/python3
"""This script reads response header value """


if __name__ == "__main__":
    from urllib import request, response
    from sys import argv

    URL = argv[1]

    with request.urlopen(URL) as response:
        print(response.headers["X-Request-Id"])
