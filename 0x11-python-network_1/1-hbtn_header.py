#!/usr/bin/python3
""" A script that takes in a URL,\
    sends a request to the URL \
    and displays the value of the X-Request-Id variable \
    found in the header of the response.
"""
import sys
from urllib.request import urlopen


if __name__ == '__main__':
    with urlopen(sys.argv[1]) as res:
        result = res.headers
        print(result['X-Request-Id'])
