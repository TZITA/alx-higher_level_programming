#!/usr/bin/python3
""" A script that fetches https://alx-intranet.hbtn.io/status"""
from urllib.request import urlopen


if __name__ == '__main__':
    with urlopen('https://alx-intranet.hbtn.io/status') as res:
        result = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(result)))
        print("\t- content: {}".format(result))
        print("\t- utf8 content: {}".format(result.decode("utf-8")))
