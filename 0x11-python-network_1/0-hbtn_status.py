#!/usr/bin/python3
""" A script that fetches https://alx-intranet.hbtn.io/status."""
import urllib.request


if __name__ == '__main__':
    r = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        result = res.read()
