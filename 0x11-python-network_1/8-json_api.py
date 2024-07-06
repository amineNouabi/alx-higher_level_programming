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

    if r.status_code == 204:
        print("No result")
    elif r.headers["Content-Type"] != "application/json":
        print("Not a valid JSON")
    else:
        try:
            res_json = r.json()
            res_keys = res_json.keys()
            if "id" in res_keys and "name" in res_keys:
                print("[{}] {}".format(res_json["id"], res_json["name"]))
            else:
                print("No result")
        except Exception:
            print("Not a valid JSON")
