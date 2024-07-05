#!/usr/bin/python3
"""This script prints content of response
    if status is success otherwise prints error code"""


if __name__ == "__main__":
    from sys import argv
    from requests import post

    URL = "http://0.0.0.0:5000/search_user"
    q = ""
    try:
        q = argv[1]
    except IndexError:
        pass

    data = {"q": q}
    r = post(URL, data=data)

    try:
        res_json = r.json()
        if "id" in res_json.items() and "name" in res_json.items():
            print("[{}] <{}>".format(res_json["id"], res_json["name"]))
        else:
            print("No result")
    except Exception as e:
        print("Not a valid JSON")
