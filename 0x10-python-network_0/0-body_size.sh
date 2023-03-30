#!/bin/bash
# Takes in a URL, sends a request, and displays the size
curl -Is $1 | grep -o '(?<=Content-Length: )\d+'
