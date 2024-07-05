#!/usr/bin/python3
"""This script prints rensponse body of a predefined URL"""


if __name__ == "__main__":
    from sys import argv
    from urllib.error import HTTPError
    from urllib.request import urlopen, Request

    URL = argv[1]

    try:
        request = Request(URL)
        with urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
