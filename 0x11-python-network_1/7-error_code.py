#!/usr/bin/python3
"""
    A Python script that takes in a URL, sends a request
    to the URL and displays the body of the response.
    Handling errors.
"""
import sys
import requests


if __name__ == "__main__":
    try:
        res = requests.get(sys.argv[1])
        res.raise_for_status()
        print(res.content.decode('utf-8'))

    except requests.exceptions.HTTPError as err:
        print(f"Error code: {err.response.status_code}")
