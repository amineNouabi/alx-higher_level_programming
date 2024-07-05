#!/usr/bin/python3
"""This script prints rensponse body of a predefined URL"""


if __name__ == "__main__":
    from urllib import request, response

    URL = "https://alx-intranet.hbtn.io/status"
    body = ""
    with request.urlopen(URL) as response:
        body = response.read()

    print("Body response:")
    print("    - type: {}".format(type(body)))
    print("    - content: {}".format(body))
    print("    - utf8 content: {}".format(body.decode("utf-8")))
