#!/usr/bin/python3
"""This script prints rensponse body of a predefined URL using requests"""


if __name__ == "__main__":
    import requests

    URL = "https://alx-intranet.hbtn.io/status"
    r = requests.get(URL)
    print(r.headers["X-Request-Id"])
