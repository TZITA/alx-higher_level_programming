#!/usr/bin/python3
""" A Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    res = requests.get('https://alx-intranet.hbtn.io/status')
    result = res.content.decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(type(result)))
    print("\t- content: {}".format(result))
