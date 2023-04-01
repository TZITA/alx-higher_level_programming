#!/usr/bin/python3
"""
    A Python script that takes in a URL, sends a request to the URL
    and displays the value of the variable X-Request-Id in the response header
"""
import sys
import requests


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    result = res.headers['X-Request-Id']
    if result:
        print(result)
    else:
        pass
