#!/usr/bin/python3
"""This script prints rensponse body of a predefined URL"""


if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from sys import argv

    URL = argv[1]
    email = argv[2]

    data = urlencode({"email": email}).encode("utf-8")

    req = Request(URL, data=data)
    with urlopen(req) as response:
        print(response.read().decode("utf-8"))
