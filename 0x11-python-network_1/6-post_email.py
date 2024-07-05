#!/usr/bin/python3
"""This script post an email to the URL"""


if __name__ == "__main__":
    from sys import argv
    import requests

    URL = argv[1]
    data = {
        "email": argv[2]
    }

    r = requests.post(URL, data=data)
    print(r.text)
