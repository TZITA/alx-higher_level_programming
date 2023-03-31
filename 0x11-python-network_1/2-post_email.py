#!/usr/bin/python3
""" A script that takes in a URL and an email, \
    sends a POST request to the passed URL with \
    the email as a parameter, and displays the \
    body of the response (decoded in utf-8).
"""
import sys
from urllib.request import urlopen
from urllib.parse import urlencode


if __name__ == '__main__':
    val = {"email": sys.argv[2]}
    d = urlencode(val).encode("ascii")

    with urlopen(sys.argv[1], d) as res:
        print(res.read().decode("utf-8"))
