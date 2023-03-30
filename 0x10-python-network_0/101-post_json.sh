#!/bin/bash
# send a POST request with contents of file, filename is second argument
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
