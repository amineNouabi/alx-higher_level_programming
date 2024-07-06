#!/usr/bin/python3
"""Get """


if __name__ == "__main__":
    from sys import argv
    from requests import get

    URL = "https://api.github.com/user"
    username = argv[1]
    token = argv[2]

    headers = {
        "Authorization": "Bearer {}".format(token),
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    try:
        r = get(URL, headers=headers)
        user = r.json()
        print(user["id"])
    except Exception:
        print("None")
