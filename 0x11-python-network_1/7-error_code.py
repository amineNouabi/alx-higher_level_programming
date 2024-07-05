#!/usr/bin/python3
"""This script prints content of response
    if status is success otherwise prints error code"""


if __name__ == "__main__":
    from sys import argv
    import requests

    URL = argv[1]
    r = requests.get(URL)

    pre_status_code = r.status_code // 100
    if pre_status_code in [4, 5]:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
