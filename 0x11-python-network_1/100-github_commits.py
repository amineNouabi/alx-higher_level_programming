#!/usr/bin/python3
""" This script lists 10 recent commits of a github repo owner:repo"""


if __name__ == "__main__":
    from sys import argv
    from requests import get

    repo = argv[1]
    owner = argv[2]

    URL = "https://api.github.com/repos/{}/{}/commits?per_page=10".format(
        owner, repo)
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    try:
        response = get(URL, headers=headers)
        commits = response.json()
        if len(commits) > 10:
            commits = commits[:10]
        for commit in commits:
            print(commit["sha"] + ": " + commit["commit"]["author"]["name"])
    except Exception:
        pass
