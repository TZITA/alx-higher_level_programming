#!/bin/bash
# send a POST request with contents of file, filename is second argument
curl -sX POST "$1" -d "$2"
