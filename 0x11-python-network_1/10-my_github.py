#!/usr/bin/python3
""" A script  takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id.
"""
import requests
import sys


if __name__ == "__main__":
    res = requests.get('https://api.github.com/users/{}'.format(sys.argv[1])).json()
    print(res['id'])
