#!/usr/bin/python3
""" A script  takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id.
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]

    url = 'https://api,github.com/user'
    res = requests.get(url, auth=(username, passwd))

    if res.status_code == 200:
        response = res.json()
        print(response['id'])
    else:
        print("None")