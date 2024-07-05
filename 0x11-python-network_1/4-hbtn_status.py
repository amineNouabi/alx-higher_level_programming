#!/usr/bin/python3
"""This script prints rensponse body of a predefined URL using requests"""


if __name__ == "__main__":
    import requests

    URL = "https://alx-intranet.hbtn.io/status"
    r = requests.get(URL)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
