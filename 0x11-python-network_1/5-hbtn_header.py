#!/usr/bin/python3
"""This script prints rensponse header of a predefined URL using requests"""


if __name__ == "__main__":
    from sys import argv
    import requests

    URL = argv[1]
    r = requests.get(URL)

    try:
        print(r.headers["X-Request-Id"])
    except KeyError:
        pass
