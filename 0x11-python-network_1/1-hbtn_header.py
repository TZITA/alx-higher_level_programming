#!/usr/bin/python3
""" A script that takes in a URL,\
    sends a request to the URL \
    and displays the value of the X-Request-Id variable \
    found in the header of the response.
"""
import sys
import urllib.request


if __name__ == '__main__':
    r = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(r) as res:
        result = dict(res.headers).get("X-Request-Id") 
        print("{}".format(result))
