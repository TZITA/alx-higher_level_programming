#!/usr/bin/python3
""" A Python script that takes in a letter
    and sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 2:
        val = sys.argv[1]
        res = requests.post('http://0.0.0.0:5000/search_user', data={"q": val})
    else:
        res = requests.post('http://0.0.0.0:5000/search_user')
    try:
        json_d = res.json()
        if json_d == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_d['id'], json_d['name']))
    except ValueError:
        print("Not a valid JSON")
