#!/usr/bin/python3
""" List 10 commits """
import sys
import requests


if __name__ == "__main__":
    url = "https://developer.github.com/v3/{}/{}".format(sys.argv[1], sys.argv[2])
    res = requests.get(url).json()

