#!/usr/bin/python3
"""This script prints content of response
    if status is success otherwise prints error code"""


if __name__ == "__main__":
    from sys import argv
    import requests

    URL = argv[1]
    r = requests.get(URL)

    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
